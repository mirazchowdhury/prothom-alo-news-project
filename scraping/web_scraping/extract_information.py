from db_connection import create_db_connection
from requests_html import HTMLSession

def insert_data(connection, title, links):
    """
    Inserts scraped data into the MySQL database.

    Parameters:
    connection : mysql.connector.connection.MySQLConnection
        The database connection.
    title : str
        The title of the webpage.
    links : list of tuples
        List of (link_text, link_href) tuples.

    Returns:
    None
    """
    try:
        cursor = connection.cursor()

        # Insert title
        if title:
            print("Inserting title into database:", title)
            cursor.execute("INSERT INTO scraped_data (title) VALUES (%s)", (title,))
            print(f"Title inserted successfully.")
        else:
            print("No title found. Skipping title insertion.")

        # Insert links
        valid_links = [(link_text, link_href) for link_text, link_href in links if link_text and link_href]
        if valid_links:
            for link_text, link_href in valid_links:
                print(f"Inserting link: {link_text}, {link_href}")
                cursor.execute(
                    "INSERT INTO scraped_data (link_text, link_href) VALUES (%s, %s)",
                    (link_text, link_href),
                )
        else:
            print("No valid links to insert.")

        # Commit changes
        connection.commit()
        print("Data committed successfully.")
    except Exception as e:
        print(f"An error occurred during data insertion: {e}")
    finally:
        cursor.close()

def extract_information(url):
    """
    Extracts and stores specific information from a webpage using CSS selectors.

    Parameters:
    url : str
        The URL of the website to scrape.

    Returns:
    None
    """
    session = HTMLSession()
    connection = create_db_connection()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        response = session.get(url)

        # Extracting the title
        # Adjusted to find div with class 'container' and span with class 'title-no-link-parent'
        title_element = response.html.find('span.tilte-no-link-parent', first=True)
        
        print(f"Page Title: {title_element}")

        # Extracting all links
        links = response.html.find('a')
        extracted_links = [
            (link.text.strip(), link.attrs.get('href', '').strip()) for link in links if link.attrs.get('href')
        ]
        print(f"Extracted Links: {len(extracted_links)} links found.")

        # Store data in the database
        insert_data(connection, title_element, extracted_links)
    except Exception as e:
        print(f"An error occurred during scraping: {e}")
    finally:
        session.close()
        connection.close()

if __name__ == "__main__":
    # Replace the URL with your desired webpage
    extract_information('https://www.prothomalo.com/bangladesh/crime')

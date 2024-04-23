import requests
from bs4 import BeautifulSoup


def extract_plugin_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        plugin_links = []
        table = soup.find("table", {"role": "table"})
        if table:
            rows = table.find_all("tr")
            for row in rows[1:]:  # Skip header row
                cells = row.find_all("td")
                if len(cells) >= 2:  # Check if there are at least two cells
                    download_link = cells[-2].find("a")
                    if download_link:
                        plugin_links.append(download_link["href"])
        return plugin_links
    else:
        print("Failed to fetch the webpage")
        return None


def write_links_to_file(links, filename):
    with open(filename, "w") as file:
        for link in links:
            file.write(link + "\n")


if __name__ == "__main__":
    webpage_url = (
        "https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins"
    )
    output_filename = "plugin_links.txt"
    links = extract_plugin_links(webpage_url)
    if links:
        write_links_to_file(links, output_filename)
        print(f"Plugin links have been written to {output_filename}")
    else:
        print("No plugin links found")

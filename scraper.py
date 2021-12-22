from savepagenow import capture
import json
import time

wait_time = 6

def scrape_list(url_list):
    success_list = list()
    repeat_list = list()

    for index, url in enumerate(url_list):
        try:
            print(index+1, url, end=" ")
            archive_url = capture(url)
            success_list.append(archive_url)
            print("\tY")
        except:
        #except WaybackRuntimeError as e:
            repeat_list.append(url)
            print("\tN")
        time.sleep(wait_time)
    print(f"URLs queued: {len(success_list)}\nURLs to redo: {len(repeat_list)}")


if __name__=="__main__":
    url_list = None

    with open("url_list.json") as f:
        url_list = json.load(f)

    print(f"Number of URLs loaded: {len(url_list)}")

    scrape_list(url_list)

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


def scrape_mjm(pages=20):
    main_url = "https://jobwebkenya.com/jobs/"
    jobs = []

    for page in range(1, pages + 1):
        url = f"{main_url}page/{page}/"
        print(f"Scraping MyJobMag page {page}")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        all_jobs = soup.find("ol", class_="jobs")
        if not all_jobs:
            continue

        vacancies = all_jobs.find_all("li", class_="job")
        for vacancy in vacancies:
            job_name = vacancy.find("div", id="titlo")
            location = vacancy.find("div", id="location")

            job_data = {
                "Job": job_name.text.strip() if job_name else "",
                "Location": location.text.strip() if location else ""
            }

            jobs.append(job_data)

    return jobs




# def scrape_bmonday(pages=10):
#     main_url="https://www.brightermonday.co.ke/jobs"
#     jobs=[]

#     for page in range(1, pages + 1):
#         url=f"{main_url}?page={page}"
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, "html.parser")

#         all_jobs = soup.find("div", class_="container")
#         if not all_jobs:
#             continue

#         vacancies = all_jobs.find_all("div", class_="w-full")
#         for vacancy in vacancies:
#             job_name = vacancy.find("span", class_="absolute inset-0")
#             location = vacancy.find("span", class_="mb-3 px-3 py-1 rounded bg-brand-secondary-100 mr-2 text-loading-hide")

#             job_data = ({
#                 "Job": job_name.text.strip() if job_name else ""},
#                 {"Location": location.text.strip() if location else ""
#             })


#             jobs.append(job_data)

#     return jobs




@app.route("/")
def home():
    jobs_mjm = scrape_mjm(pages=20)  
    all_jobs = jobs_mjm 
    return render_template("job.html", jobs=all_jobs)

if __name__ == "__main__":
    app.run(debug=True)

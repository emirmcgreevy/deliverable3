import csv
import os
import glob

def process_athlete_data(file_path):
    records = []
    races = []
    athlete_name = ""
    athlete_id = ""
    comments = ""

    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)

        athlete_name = data[0][0]
        athlete_id = data[1][0]
        print(f"The athlete id for {athlete_name} is {athlete_id}")

    return {
        "name": athlete_name,
        "athlete_id": athlete_id
    }

def gen_team_roster_page(athletes, outfile, title):
    html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="https://kit.fontawesome.com/91e0ab759a.js" crossorigin="anonymous"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Skyline High School Cross Country</title>
    <link rel="stylesheet" href="../css/reset.css">
    <link rel="stylesheet" href="../css/stylesheet.css">
</head>
<body>
    <header>
        <h1>
            <img src="images/skyline_logo.png" alt="Skyline High School Ann Arbor Logo" class="logo">
            Skyline High School Cross Country
        </h1>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="mens_roster.html">Men's Team</a></li>
                <li><a href="womens_roster.html">Women's Team</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <h2>{title}</h2>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                </tr>
            </thead>
            <tbody>
        '''

    for athlete in athletes:
        # Each athlete's name is added into the table body as a row
        html_content += f'''
                <tr>
                    <td><a href="{athlete["profile_url"]}">{athlete["name"]}</a></td>
                </tr>
        '''

    html_content += '''
            </tbody>
        </table>
    </main>
    <footer>
        <p>
            Skyline High School<br>
            <address>
                2552 North Maple Road<br>
                Ann Arbor, MI 48103<br><br>
            </address>
            <a href="https://www.instagram.com/a2skylinexc/" aria-label="Follow us on Instagram">
                <i class="fa-brands fa-instagram" aria-hidden="true"></i>
            </a>
        </p>
    </footer>
    <script src="/js/script.js"></script>
    </body>
    </html>
    '''

    with open(outfile, 'w') as output:
        output.write(html_content)



def main():
    # Generate Men's Team Roster Page
    folder_path = 'mens_team/'
    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
    athletes = []

    for file in csv_files:
        athlete_data = process_athlete_data(file)
        filename = os.path.basename(file).replace('.csv', '.html')
        athlete_data['profile_url'] = os.path.join(folder_path, filename)
        athletes.append(athlete_data)

    gen_team_roster_page(athletes, 'mens_roster.html', "Men's Team Roster")

    # Generate Women's Team Roster Page
    folder_path = 'womens_team/'
    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
    athletes = []

    for file in csv_files:
        athlete_data = process_athlete_data(file)
        filename = os.path.basename(file).replace('.csv', '.html')
        athlete_data['profile_url'] = os.path.join(folder_path, filename)
        athletes.append(athlete_data)

    gen_team_roster_page(athletes, 'womens_roster.html', "Women's Team Roster")

if __name__ == '__main__':
    main()

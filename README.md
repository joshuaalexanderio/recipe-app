# Recipe App

A Flask web application that displays recipe cards using CSS Grid and integrates with Todoist to automatically add ingredients to your shopping list.

## Features
- **Recipe Grid Display:** Clean layout showcasing frequently used recipes
- **One-Click Shopping Lists:** Export all recipe ingredients directly to Todoist
- **Todoist Integration:** Seamlessly adds ingredients to your designated project
- **Responsive Design:** CSS Grid layout adapts to different screen sizes

## Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS Grid, JavaScript
- **API Integration:** Todoist REST API
- **Web Scraping:** BeautifulSoup4

## Getting Started

### Prerequisites
- Python 3.x
- Todoist account
- Todoist API token ([Get one here](https://todoist.com/app/settings/integrations)

### Installation
1. Clone the repository and navigate to the main directory
2. Install dependencies:
   pip install flask bs4

### Configuration

Update the Authorization token in todoist.py
Run python todoist.py to see your available projects
Copy the project_id for your desired shopping list

Update server configuration:
In server.py, replace all "Authorization" values with Bearer [your_token]
Replace all "project_id" values with your chosen project ID

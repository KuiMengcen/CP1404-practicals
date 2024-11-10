import datetime
from prac_07.project import Project


MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n" \
       "- (A)dd new project\n- (U)pdate project\n- (Q)uit"

def main():
    filename = "projects.txt"
    projects = load_projects(filename)

    print(MENU)
    choice = input(">>> ").strip().lower()
    while choice != "q":
        if choice == "l":
            projects = load_projects(filename)
        elif choice == "s":
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            try:
                date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
                filter_projects_by_date(projects, date)
                display_projects(projects)
            except ValueError:
                print("Invalid date format. Please use dd/mm/yyyy.")
        elif choice == "a":
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>> ").strip().lower()
    save_projects(filename, projects)
    print("Thank you for using custom-built project management software.")
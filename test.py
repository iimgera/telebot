from works.models import Project



if __name__ == '__main__':
    projects = Project.objects.all()
    # выводим заголовки всех проектов
    for project in projects:
        print(project.title)

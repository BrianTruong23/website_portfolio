

class Project:
    def __init__(self, big_title, year, category,description,award,img_url,source_url,demonstration_url,name):
        self.big_title = big_title
        self.name = name
        self.year = year
        self.category = category
        self.description = description
        self.img_url = img_url
        self.award = award
        self.source_url = source_url
        self.demonstration_url = demonstration_url




project_1 = Project(
    big_title = "To-Do List App",
    name = "GetDoneTask",
    year = "2018",
    category = "To Do List",
    description = "As part of exploring more about coding, I work on my first personal project which is an Iphone App using Swift and Xcode. The app implements many features including Core Data Database and CocoaPods. The most interesting feature would be swiping tasks like swiping Tinder dates. The app helps me win Congressional App Challenge Texas District 2",
    img_url = "static/images/congress_2.JPG",
    award = "Congressional Winner",
    source_url = "https://bitbucket.org/brian1223/getdonetask/src/master/",
    demonstration_url = "https://vimeo.com/manage/videos/377679963"
)

project_2 = Project(
    big_title = "Blog",
    name = "Thang's Blog",
    year = "2021",
    category = "Blog Website",
    description = "The blog is built as a project from Python Course on Udemy by Angela Yu. It is built by HTML, CSS, and Python with Flask handling the back-end and user registration. It also uses Sqlalchemy to store the database of the users. The blog is where I share my voice. This is where I talk to the world.",
    img_url = "static/images/blog.jpg",
    award = "My Diary",
    source_url = "https://github.com/BrianTruong23/thang-blog",
    demonstration_url = "https://thang-blog.herokuapp.com/"
)

project_3 = Project(
    big_title = "VieTalk Website",
    name = "Thang's Blog",
    year = "2021",
    category = "Blog Website",
    description = "The blog is built as a project from Python Course on Udemy by Angela Yu. It lets the user register to make comment. It is built by HTML, CSS, and Python with Flask handling the back-end. It also uses Sqlalchemy to store the database of the users. The blog is where I share my voice. This is where I talk to the world.",
    img_url = "static/images/blog.jpg",
    award = "My Diary",
    source_url = "https://github.com/BrianTruong23/thang-blog",
    demonstration_url = "https://thang-blog.herokuapp.com/"
)





projects_list = [project_1,project_2, project_3]



## CourseCatalog

A simple python script to save sample course catalog data to MongoDB.

The script pulls data from the the json file (courses.json) and uses the Python [faker](https://github.com/joke2k/faker) library to generate fake student profile information, courses taken, and grades.

### MongoDB Schema

The script creates several MongoDB collections, such as `course`, `student`, and `course_taken`. 

#### `course` collection

Documents in the `course` collection represent an individual course being offered.

Example:

~~~
[
    {
    "_id": "1",
    "course_code": "INF-3792",
    "university": "University of Tromsø",
    "course_name": "Medical Informatics",
    "course_semester": "Spring2019"
    },
    {
    "_id": "2",
    "course_code": "INF-3795",
    "university": "University of Tromsø",
    "course_name": "Advanced telemedicine and e-health systems",
    "course_semester": "Spring2019"
    },
    {
    "_id": "3",
    "course_code": "INF-3910",
    "university": "University of Tromsø",
    "course_name": "Advanced telemedicine and e-health systems",
    "course_semester": "Spring2019"
    },
    {
    "_id": "4",
    "course_code": "IN4080",
    "university": "University of Oslo",
    "course_name": "Natural Language Processing",
    "course_semester": "Spring2019"
    },
    {
    "_id": "5",
    "course_code": "IN5020",
    "university": "University of Oslo",
    "course_name": "Distributed Systems",
    "course_semester": "Spring2019"
    },
    {
    "_id": "6",
    "course_code": "IN5290",
    "university": "University of Oslo",
    "course_name": "Ethical Hacking",
    "course_semester": "Spring2019"
    },
    {
    "_id": "7",
    "course_code": "INF5013NSA",
    "university": "University of Oslo",
    "course_name": "Cyberethics",
    "course_semester": "Autumn2019"
    },
    {
    "_id": "8",
    "course_code": "IN5520",
    "university": "University of Oslo",
    "course_name": "Digital Image Analysis",
    "course_semester": "Autumn2019"
    },
    {
    "_id": "9",
    "course_code": "IT2805",
    "university": "NTNU",
    "course_name": "Web Technologies",
    "course_semester": "Spring2019"
    },
    {
    "_id": "10",
    "course_code": "T3105",
    "university": "NTNU",
    "course_name": "Artificial Intelligence Programming",
    "course_semester": "Spring2019"
    },
    {
    "_id": "11",
    "course_code": "IMT3601",
    "university": "NTNU",
    "course_name": "Game Programming",
    "course_semester": "Autumn2019"
    },
    {
    "_id": "12",
    "course_code": "IMT2681",
    "university": "NTNU",
    "course_name": "Cloud Technologies",
    "course_semester": "Autumn2019"
    }
]
~~~

#### `student` collection

Documents in this collection represent an individual student. Note that all information is randomly generated.

Example:

~~~

~~~

#### `course_taken` collection

Documents in this collection correspond to a single session of a course taken by a student. This includes the date the course was taken and the grade the student received.

Example:

~~~
{
	"_id" : ObjectId("577483b54c3b8252e9902ba3"),
	"student_id" : "44521640-3e6a-11e6-8fbe-acbc327f8c19",
	"grade" : "praesentium",
	"course_id" : ObjectId("577483b14c3b8252e9902a93"),
	"date_completed" : ISODate("1984-03-16T17:09:50Z")
}
~~~

## Note

All data from the Coursera API is owned by the original copyright holders.

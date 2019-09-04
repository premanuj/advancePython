import json
import xml.etree.ElementTree as et

class Course:
    def __init__(self, course_id, title, duration):
        self.course_id = course_id
        self.title= title
        self.duration = duration

class CourseSerializer:
    def serialize(self, course, format_):
        serializer = self._get_serializer(format_)
        return serializer(course)
        
    def _get_serializer(self, format_):
        if format_.upper() == "JSON":
            return self._serialize_to_json
        elif format_.upper() == "XML":
            return self._serialize_to_xml
        else:
            raise ValueError("Invalid Format")
            
    def _serialize_to_json(self, course):
        course_info = {
                    "id": course.course_id,
                    "title": course.title,
                    "duration": course.duration
                }
        return json.dumps(course_info)
    
    def _serialize_to_xml(self, course):
        course_info = et.Element('course', attrib={'id': str(course.course_id)})
        title = et.SubElement(course_info, 'title')
        title.text = course.title
        duration = et.SubElement(course_info, 'duration')
        duration.text = course.duration
        return et.tostring(course_info, encoding='unicode')

course = Course(1, "Python", "3w")

serializer = CourseSerializer()

print("================JSON==============")
print(serializer.serialize(course, "json"))

print("================XML==============")
print(serializer.serialize(course, "xml"))
class Course:
    def __init__(self, course_id, title, duration):
        self.course_id = course_id
        self.title= title
        self.duration = duration
    
    def serialize(self, serializer):
        serializer.start_object("song", self.course_id)
        serializer.add_property("title", self.title)
        serializer.add_property("duration", self.duration)
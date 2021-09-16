from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

class Mark(models.Model):
    roll_number = models.CharField(max_length=10,)
    name = models.CharField(max_length=30,)
    phone = models.IntegerField()
    subject_name = models.CharField(max_length=30,)


    mark = models.CharField(max_length=20, null= True)
    semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],)
    cat = models.CharField(max_length=20)

    def __str__(self):
        return str(self.roll_number) + "- Semester : " + str(self.semester) + " - CAT :" + str(self.cat) + " Subject : " + str(self.subject_name)




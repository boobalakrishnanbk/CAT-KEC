from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

class Mark(models.Model):
    roll_number = models.CharField(max_length=10,)
    name = models.CharField(max_length=30,)
    phone = models.IntegerField()
    subject_name = models.CharField(max_length=30,)


    mark = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],null=True)
    semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],)
    cat = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)],)

    def __str__(self):
        return str(self.roll_number) + "- Semester : " + str(self.semester) + " - CAT :" + str(self.cat) + " Subject : " + str(self.subject_name)




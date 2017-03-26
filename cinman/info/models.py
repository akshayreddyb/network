from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Machine(models.Model):
    ip_address=models.CharField(max_length=20)
    mac_address=models.CharField(max_length=40)
    ram_description=models.CharField(max_length=50)
    ram_capacity=models.IntegerField()
    disk_capacity=models.IntegerField()
    disk_used_amount=models.IntegerField()
    disk_description=models.CharField(max_length=50)
    motherboard_description=models.CharField(max_length=50)
    cpu_name=models.CharField(max_length=50)
    cpu_cores=models.CharField(max_length=50)
    cpu_clock_speed=models.IntegerField()
    os_name=models.CharField(max_length=20)
    os_version=models.CharField(max_length=25)

class Softwaresinstalled(models.Model):
    machine=models.ForeignKey(Machine, null=False, blank=False, related_name="softwares_installed")
    name=models.CharField(max_length=25)
    update_available=models.BooleanField(default=False)
    version=models.CharField(max_length=20)

class Peripherals(models.Model):
    PERIPHERAL_CHOICES=(
        (1,"Keyboard"),
        (2,"Mouse"),
        (3,"Speaker")
    )
    machine = models.ForeignKey(Machine, null=False, blank=False, related_name="peripherals")
    type=models.IntegerField(choices=PERIPHERAL_CHOICES)
    presence=models.BooleanField(default=True)

class MachineUser(models.Model):
    username=models.CharField(max_length=30)
    last_login_time=models.DateTimeField()

class UsersActiveOn(models.Model):
    username=models.ForeignKey(MachineUser,related_name="active_users")
    machine=models.ForeignKey(Machine,related_name="active_machines")

class Session(models.Model):
    username=models.ForeignKey(MachineUser,related_name="session_user")
    machine=models.ForeignKey(Machine,related_name="session_machine")
    login_time=models.DateTimeField()
    logout_time=models.DateTimeField()

class Logs(models.Model):
    TYPE_CHOICES=(
            (1,"General message and system related logs"),
            (2,"Authentication Logs"),
            (3,"Login Records"),
            (4,"MySQL database server log file"),
            (5,"Kernal Logs"),
            (6,"System boot Log"),
            (7,"dpkg"),
            (8,"Mail Server Logs")

    )
    session=models.ForeignKey(Session,related_name="log_session")#fill
    username=models.ForeignKey(MachineUser,related_name="userlogs")
    machine=models.ForeignKey(Machine,related_name="machinelogs")
    content=models.CharField(max_length=500)
    type=models.IntegerField(choices=TYPE_CHOICES)

class Messages(models.Model):
    session=models.ForeignKey(Session,related_name="message_session")#fill
    username=models.ForeignKey(MachineUser,related_name="user_messages")
    machine=models.ForeignKey(Machine,related_name="machine_messages")
    content=models.CharField(max_length=100)
    time=models.DateTimeField()

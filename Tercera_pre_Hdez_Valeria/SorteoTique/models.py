from django.db import models

# Create your models here.

#tipo de sorteo "sorteo gana efectivo"/ "sorteo iPremios"/ "sorteo aventura" / "sorteo educativo" / "sorteo mi futuro"
class Draw(models.Model):
    draw_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
   
#cliente, quien compra boleto registrarse es requisito
class Client(models.Model):
    client_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return f"id_cliente: {self.client_id} - nombre: {self.name} - apellido: {self.last_name} - email: {self.email}"
    #pwd = models.CharField(max_length=30)
    #pwd_question = models.CharField(max_length=30)

#quien vende el boleto
class Seller(models.Model):
    seller_id = models.CharField(max_length=30)
    seller_name = models.CharField(max_length=30)
    seller_last_name = models.CharField(max_length=30)
    email = models.EmailField()
   # pwd = models.CharField(max_length=30)
    
#lista de premios de todos los sorteos
class Prize(models.Model):
    prize_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.EmailField()

#boleto
class Ticket(models.Model):
    ticket_id = models.CharField(max_length=30)
    cost = models.IntegerField()
    available = models.BooleanField()
    
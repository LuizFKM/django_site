from django.db import models
from django.contrib.auth.models import User

STATUS = ( #rascunho ou publicado
    (0, 'Draft'),
    (1, 'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True) #identificação do post, slug aceita texto e caracteres adicionais
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') #autor do post
    update_on = models.DateTimeField(auto_now=True) #campo de data, quando foi atualizado
    content = models.TextField() #conteudo, textfield um campo espcial para texto
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0) #campo para inteiros, choices é um array de objetos que construimos a estrutura para associar o tipo do status. 

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self): #retorna o título dos posts.
        return self.title


from .models import Info

def add_visit(post):
    post.visits += 1
    post.save()

    visitas = Info.objects.get(key="visitas")
    visitas_int = int(visitas.value)
    visitas.value = visitas_int + 1
    visitas.save()
from django.shortcuts import render
from .models  import Track,Curse, Video


# Create your views here.



def show_tracks(request):
    tracks=Track.objects.all()
    
    return render(request,"home.html",{"tracks":tracks})



def show_curses(request,track_id):
    track=Track.objects.get(id=track_id)
    curses=Curse.objects.filter(track__id=track_id)

    return render(request,"track_curses.html",{"curses":curses,"track":track})



def show_current_video(request,track_id,curse_id):
    
    track=Track.objects.get(id=track_id)
    curse=Curse.objects.filter(id=curse_id)
    current_video=Video.objects.filter(curse__in=curse).first()


    return render(request,"curse.html",{"current_video":current_video,"track":track,"curse":curse })


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.reverse import reverse

from master.models import Snippest, Tags
  
  
# class HelloView(APIView):
#     permission_classes = (IsAuthenticated, )
  
#     def get(self, request):
#         content = {'message': 'Hello, GeeksforGeeks'}
#         return Response(content)


class SnippetsView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self,request):
        
        host = request.META['HTTP_HOST']
        snippets_list = []
        snipets_obj = Snippest.objects.all()
        for snippet in snipets_obj:
            data = {
                'id':snippet.id,
                'title':snippet.title,
                'short_text':snippet.short_text,
                'tag':snippet.tags.tag_title,
                'timestamp':snippet.time_stamp,
                'user':snippet.user_id.username,
                'url': host+'/snipets_details/'+str(snippet.id)
            }
            snippets_list.append(data)

        return Response({'snippets_count':len(snipets_obj),'records':snippets_list})
    
    def post(self,request):
        try:
            title = request.POST.get('title')
            short_text = request.POST.get('short_text')
            if Tags.objects.filter(tag_title=title).exists():
                tag_obj = Tags.objects.get(tag_title=title)
            else:
                tag_obj = Tags.objects.create(tag_title= title)

            snippets_obj = Snippest.objects.create(
                title=title,
                short_text=short_text,
                tags = tag_obj,
                user_id = request.user,
            )        
            return Response({'message':'Successfully Created Snippets','status':'success'})
        except Exception as e:
            return Response({'message':str(e),'status':'failure'})




class DetailView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self,request,pk):
        snippets_ = Snippest.objects.filter(id = pk).values('title','short_text','time_stamp')

        return Response({'status':snippets_})

    def put(self,request,pk):
        try:
            title = request.POST.get('title')
            short_text = request.POST.get('short_text')
            if Tags.objects.filter(tag_title=title).exists():
                tag_obj = Tags.objects.get(tag_title=title)
            else:
                tag_obj = Tags.objects.create(tag_title= title)

            snippets_obj = Snippest.objects.get(id=pk)
            snippets_obj.title = title
            snippets_obj.short_text = short_text
            snippets_obj.user_id = request.user
            snippets_obj.tags = tag_obj
            snippets_obj.save()
            snippets_obj = Snippest.objects.filter(id=pk).values('title','short_text','time_stamp')

            return Response({'status':'Successfully Updated The Snippets','item_detail':snippets_obj})

        except Exception as e:
            return Response({'message':str(e),'status':'failure'})

    def delete(self,request,pk):
        try:
            snipets_obj = Snippest.objects.get(id=pk)
            snipets_obj.delete()
            host = request.META['HTTP_HOST']
            snippets_list = []
            snipets_obj = Snippest.objects.all()
            for snippet in snipets_obj:
                data = {
                    'id':snippet.id,
                    'title':snippet.title,
                    'short_text':snippet.short_text,
                    'tag':snippet.tags.tag_title,
                    'timestamp':snippet.time_stamp,
                    'user':snippet.user_id.username,
                    'url': host+'/snipets_details/'+str(snippet.id)
                }
                snippets_list.append(data)

            return Response({'snippets_count':len(snipets_obj),'records':snippets_list})

        except Exception as e:
            return Response({'message':str(e),'status':'failure'})


class TagView(APIView):

    def get(self,request):
        try:
            tags_list = Tags.objects.all().values('id','tag_title')
            return Response({'records':tags_list})
        except Exception as e:
            return Response({'message':str(e),'status':'failure'})

class TagDetails(APIView):

    def get(self,request,pk):
        try:
            snipets_list = Snippest.objects.filter(tags__id=pk).values('title','short_text','time_stamp')
            return Response({'records':snipets_list})
        except Exception as e:
            return Response({'message':str(e),'status':'failure'})



        

from flask import Blueprint,redirect,url_for,session,render_template,request,Response
from flask_login import login_required
from .Forms.CreatePost import CreatePostForm
from BlogPost.DataBase.DTO.Posts import SavePost,GetAllPost,GetPost,GetTotalPostCount,saveEditedPost
from BlogPost.Filters.Characters import CharacterLimit
import math
post_blueprint=Blueprint("post",__name__,template_folder="templates")


@post_blueprint.route("/creatpost",methods=["GET","POST"])
@login_required
def CreatePost():
    createPost=CreatePostForm()
    userid=userid=session.get('user_id',None)
    if createPost.validate_on_submit() and userid is not None:
        SavePost(createPost.Title.data,createPost.Text.data,userid)
        return redirect(url_for("post.AllPost",page=1,pageSize=5))
    return render_template("CreatePost.html",form=createPost)


@post_blueprint.route("/getposts/<int:page>/<int:pageSize>")
@login_required
def AllPost(page,pageSize):
    allPosts=GetAllPost(page,pageSize)
    print(f"Allposts:{allPosts}")
    totalrecordsCount=GetTotalPostCount()
    print(totalrecordsCount)
    totalPage=totalrecordsCount/pageSize
    totalPage=math.ceil(totalPage)
    print(totalPage)
    return render_template("AllPosts.html",posts=allPosts,totalPage=totalPage,pageno=page)

@post_blueprint.route("/viewpost/<int:postId>")
@login_required
def ViewPost(postId):
    post= GetPost(postId)
    canedit=False
    userId=session.get("user_id",None)
    if userId==post.User.Id:
        canedit=True
    return render_template("post.html",post=post,canedit=canedit)


@post_blueprint.route("/edit/<int:postId>",methods=["GET","POST"])
@login_required
def EditPost(postId):
    post= GetPost(postId)
    if post:
        editpost=CreatePostForm(formdata=request.form,obj=None,Title=post.Title,Text=post.Description)
        print(post)
        if request.method == 'POST' and editpost.validate():
            saveEditedPost(post, editpost)
            return redirect(url_for("post.AllPost",page=1,pageSize=5))
        return render_template("Edit.html",form=editpost,postid=postId)
    else:
        response = Response()
        response.status_code=404

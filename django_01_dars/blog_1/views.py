from cgitb import html
from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    html = """
        <style type="text/css">
			.fasllar{
				border: 2px solid red;
			    width: 292px; 
			    height: 50px; 
			    font-size: 40px; 
			    letter-spacing:4px; 
			    text-decoration:none;
			    background: black; 
			    color: orange; 
			    font-family: Monotype Corsiva;
			    font-weight: bold; 
			    margin:10px;
			    padding: 10px;
			    text-align: center;
                float:left;
			}
			
		</style>
        <h1 style="border: 2px solid red; width: 1300px; height: 60px; font-size: 60px; letter-spacing:4px;
		background: orange; color: black; font-family: Monotype Corsiva; font-weight: bold; margin: 10px;padding: 10px;text-align: center;">First Page</h1>
        <a href="bahor/" class="fasllar">Bahor</a>
        <a href="yoz/" class="fasllar">Yoz</a>
        <a href="kuz/" class="fasllar">Kuz</a>
        <a href="qish/" class="fasllar">Qish</a>
        
    """
    return HttpResponse(html)

def bahor(request):
    html = """
        <style type="text/css">
			.fasllar{
				border: 2px solid red;
			    width: 1300px; 
			    height: 50px; 
			    font-size: 40px; 
			    letter-spacing:4px; 
			    text-decoration:none;
			    background: orange; 
			    color: black; 
			    font-family: Monotype Corsiva;
			    font-weight: bold; 
			    margin:20px;
			    padding: 10px;
			    text-align: center;
			}
			
		</style>
        <h1 style="border: 2px solid red; width: 1300px; height: 60px; font-size: 60px; letter-spacing:4px;
		background: black; color: orange; font-family: Monotype Corsiva; font-weight: bold; margin: 20px;padding: 10px;text-align: center;">Bahor</h1>
        <a href="../" class="fasllar">First Page</a>
    """
    return HttpResponse(html)
def yoz(request):
    html = """
        <style type="text/css">
			.fasllar{
				border: 2px solid red;
			    width: 1300px; 
			    height: 50px; 
			    font-size: 40px; 
			    letter-spacing:4px; 
			    text-decoration:none;
			    background: orange; 
			    color: black; 
			    font-family: Monotype Corsiva;
			    font-weight: bold; 
			    margin:20px;
			    padding: 10px;
			    text-align: center;
			}
			
		</style>
        <h1 style="border: 2px solid red; width: 1300px; height: 60px; font-size: 60px; letter-spacing:4px;
		background: black; color: orange; font-family: Monotype Corsiva; font-weight: bold; margin: 20px;padding: 10px;text-align: center;">Yoz</h1>
        <a href="../" class="fasllar">First Page</a>
    """
    return HttpResponse(html)
def kuz(request):
    html = """
        <style type="text/css">
			.fasllar{
				border: 2px solid red;
			    width: 1300px; 
			    height: 50px; 
			    font-size: 40px; 
			    letter-spacing:4px; 
			    text-decoration:none;
			    background: orange; 
			    color: black; 
			    font-family: Monotype Corsiva;
			    font-weight: bold; 
			    margin:20px;
			    padding: 10px;
			    text-align: center;
			    
			}
			
		</style>
        <h1 style="border: 2px solid red; width: 1300px; height: 60px; font-size: 60px; letter-spacing:4px;
		background: black; color: orange; font-family: Monotype Corsiva; font-weight: bold; margin: 20px;padding: 10px;text-align: center;">Kuz</h1>
        <a href="../" class="fasllar">First Page</a>
    """
    return HttpResponse(html)
def qish(request):
    html = """
        <style type="text/css">
			.fasllar{
				border: 2px solid red;
			    width: 1300px; 
			    height: 50px; 
			    font-size: 40px; 
			    letter-spacing:4px; 
			    text-decoration:none;
			    background: orange; 
			    color: black; 
			    font-family: Monotype Corsiva;
			    font-weight: bold; 
			    margin:20px;
			    padding: 10px;
			    text-align: center;
			}
			
		</style>
        <h1 style="border: 2px solid red; width: 1300px; height: 60px; font-size: 60px; letter-spacing:4px;
		background: black; color: orange; font-family: Monotype Corsiva; font-weight: bold; margin: 20px;padding: 10px;text-align: center;">Qish</h1>
        <a href="../" class="fasllar">First Page</a>
    """
    return HttpResponse(html)
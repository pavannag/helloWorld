1. Run the python flask webapp
   python3 api.py

   http://localhost:8080 - returns hello
 
2. http://localhost:8080/healthz - Returns Json output in the requested format


4. Create a docker file to build, package, deploy, and run this application locally with Docker.
	Build the docket image as below and run the docker container.
		docker build -t app .
		docker run -d -p 8080:5000 app

# Samsung
Dockerized Flask App
You are provided with the parent-child relation of the nodes as below.
Example Relation: [{"parent": "node_1", "child": "node_4"},
   	     {"parent": "node_2", "child": "node_4"},
    	   	     {"parent": "node_3", "child": "node_4"},
   	     {"parent": "node_4", "child": "node_5"},
     {"parent": "node_4", "child": "node_7"},
    	   	     {"parent": "node_6", "child": "node_5"}]

This relation can be seen visually as below:








Your task is to create a Flask app and a function with POST method which takes the relation and the node_ids as body and return the list of nodes as Response such that each node is added to the list before their child nodes, and this creation of list should be created in parallel for each node_id in node_ids parameter using (threads or multiprocessing) module.
Example: if node_ids : [“node_5”, “node_4”]
•	 for node_5 the list will be in order ["node_1", "node_2", "node_3", "node_4", "node_6", "node_5"]
•	 for node_4 the list will be in order ["node_1", "node_2", "node_3", "node_4")
And this list creation should happen in parallel and after completion this result should be in a JSON format as shown below in example response body

This Flask app should be containerized using docker so you have to write a Dockerfile from which we can build a docker image and start using that flask app using the HTTP end point.


HTTP Request body example:
{"relation": [{"parent": "node_1", "child": "node_4"},
                  {"parent": "node_2", "child": "node_4"},
                  {"parent": "node_3", "child": "node_4"},
                  {"parent": "node_4", "child": "node_5"},
                  {"parent": "node_4", "child": "node_7"},
                  {"parent": "node_6", "child": "node_5"}],
     "node_ids": ["node_5", "node_7", "node_4"]}


Expected Response:
{"node_5": ["node_1", "node_2", "node_3", "node_4", "node_6", "node_5"],
 "node_7": ["node_1", "node_2", "node_3", "node_4", "node_7"],
 "node_4": ["node_1", "node_2", "node_3", "node_4"]
}
 



ec2instances_info = [
        {
            "id": "instance01",
            "type": "t2.micro"
        },

        {
            "id": "instance02",
            "type": "t2.medium"
        },

        {
           "id": "instance03",
           "type": "t2.large"
        }
]
print(ec2instances_info[2]["id"])     
print(ec2instances_info[1]["type"])

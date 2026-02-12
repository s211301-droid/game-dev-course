# Create the HTML file
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        .content {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <div class="content">
        <h1>Welcome to My Portfolio!</h1>
        <p>Name: XXX</p>
        <p>Student ID: 10000001</p>
        <p>Course: Game Developing with Python</p>
    </div>
</body>
</html>
"""

# Write to the HTML file
with open("portfolio.html", "w") as file:
    file.write(html_content)

print("portfolio.html has been created.")
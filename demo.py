import os
import openai

api_key = "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"

code_file = request.FILES.get('code_file')
print(code_file)
# Read the contents of the code file
# code_file_content = code_file.read().decode('utf-8')
if code_file is not None:
    code_file_content = code_file.read().decode('utf-8')
    print(code_file_content)
    # Initialize the OpenAI API client
    openai.api_key = api_key
    # Send the contents of the code file to the OpenAI API
    # response = openai.ChatCompletion.create(
    # model="gpt-3.5-turbo",
    # messages=[
    #     {"role": "system", "content": "You are a helpful assistant."},
    #     {"role": "user", "content": f"Generate a README file for the following Python code: ``{code_file_content}```"}
    # ])
    # generated_readme = response.choices[0].message.content
    # context = {
    #     'generated_readme_content': generated_readme,
    #     'generated_readme_name': 'README.md'
    # }

    # return render(request, 'readme_gen.html', context)
else:
    print("File object is None")
     

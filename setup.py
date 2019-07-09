import setuptools

#引入README.md文件
with open("README.md", "r") as fh:
    long_description = fh.read()

'''
name: 指定包名。包名只能包含字母,数字,-和_四种字符,并且包名不能与pypi.org的已有包名重复。

version: 指定包的版本号。

author: 指定作者姓名

author_email: 指定作者邮箱。author和author_email用来识别包的作者。

description: 关于包的简短描述。一般用一句话来简短概括。

long_description：关于包的详细描述。这部分信息会显示在Python Package Index上。
在本示例中，长描述写在README.md文件中，然后再通过读写文件加载进来。

long_description_content_type：用以告诉Python Package Index关于长描述的文档格式。
在本示例中，我们选择了Markdown格式。

url：用来指定这个项目的主页。对于大多数的项目而言，通常会指向Github，GitLab等。

packages：用以指出我们这个分发包所需的依赖包。相比一个个手动列出，我们可以使用 find_packages()
来自动发现所有的依赖包及其子包。

classifiers: 用以告诉 Python Package Index 和 pip 关于包更多的一些元信息。通常，你应该
包含以下信息：你的包最低可以兼容哪个版本的Python，你的包在哪种认证下可允许使用以及你的包在哪种
操作系统下可正常使用。关于 classifiers 更多的信息，可参考 https://pypi.org/classifiers/

'''
setuptools.setup(
    name="SolverDrinkingcode",
    version="1.1.0",
    author="drinkingcode",
    author_email="drinkingcode@163.com",
    description="It's an example for uploading Python Package into Python Package Index",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drinkingcode/SolverDrinkingcode",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",  #
        "License :: OSI Approved :: MIT License", #
        "Operating System :: OS Independent", #
    ],
)
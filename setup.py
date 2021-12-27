from setuptools import setup

setup(name='jupyter_MySwift_kernel',
      version='0.0.1',
      description='Minimalistic Swift kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyR-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MySwift-kernel/tarball/0.0.1',
      packages=['jupyter_MySwift_kernel'],
      scripts=['jupyter_MySwift_kernel/install_MySwift_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'Swift','ts'],
      include_package_data=True
      )

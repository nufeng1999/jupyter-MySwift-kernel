from ipykernel.kernelapp import IPKernelApp
from .kernel import MySwiftKernel
IPKernelApp.launch_instance(kernel_class=MySwiftKernel)

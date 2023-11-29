"""Setuptools setup script."""
from setuptools import find_packages, setup

setup(
    name="aot",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "torch>=2.1",
        "matplotlib",
        'opencv-python',
        'pillow',
        'spatial_correlation_sampler',
    ],
    extras_require={
        'dev': [
            'pytest',
        ],
    },
    use_scm_version=True,
    setup_requires=[
        'setuptools_scm',
    ],
    python_requires='>=3.10',
)
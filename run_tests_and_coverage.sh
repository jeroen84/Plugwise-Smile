#!/bin/sh
echo "-----------------------------------------------------------"
echo "Running Plugwise/Smile.py through pytest including coverage"
echo "-----------------------------------------------------------"
PYTHONPATH=`pwd` pytest -rpP --log-level debug tests/test_Smile.py --cov='.' --no-cov-on-fail
pytest=`echo $?`
echo "-----------------------------------------------------------------"
echo "Running Plugwise/Smile.py through flake8"
echo "-----------------------------------------------------------------"
PYTHONPATH=`pwd` flake8 --config=.flake8 Plugwise_Smile/*.py tests/*py
flake8=`echo $?`
echo "-----------------------------------------------------------------"
echo "Running Plugwise/Smile.py through pydocstyle"
echo "-----------------------------------------------------------------"
PYTHONPATH=`pwd` pydocstyle Plugwise_Smile/*.py tests/*py
pydocs=`echo $?`
echo "-----------------------------------------------------------------"
echo "Running Plugwise/Smile.py through pylint (HA-core + own disables)"
echo "-----------------------------------------------------------------"
PYTHONPATH=`pwd` pylint --rcfile=pylintrc Plugwise_Smile/*.py
pylint=`echo $?`
echo "-----------------------------------------------------------------"
echo "pytest exit code: ${pytest}"
echo "flake8 exit code: ${flake8}"
echo "pydocs exit code: ${pydocs}"
echo "pylint exit code: ${pylint}"
echo "-----------------------------------------------------------------"

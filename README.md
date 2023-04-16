# Cyclic Bandwith Problem
 Projet du module de Programmation par Contraintes du Master 1 ORO du Nantes Université

# How to run
Run from the `src` directory

Execute with :
```
python3 <model>.py <k> -data=<path+filename> -solve
```

where `<model>` is the model you want to solve with from [`model1.py`, `model1+.py`, `model2.py`, `model2+.py`, `model3.py`, `model3+.py`], `<k>` is the parameter only for the second and third models and `<path+filename>` is the path to the file containing the instance in the `.json` format. The `-solve` option is optional and allows to solve the model.
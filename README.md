# Beyond Papers 
Trying to do small gradient update to AI/ML Research with keen interest to build community of  "Code before Research paper","Random and open Experiments before perfect solution". Building value beyond papers.
 
Each algorithm will have easy to understand underlying intution and architecture breif mentioned by concept contributors and collaborators. Before moving experimental to launched atleast 3 usage examples, associated medium post and concept video will be linked in the document for quick reference. 

## Launched:
Just getting started ...

       


## Live Experiments:

### **Switchers**: 
***Compatible with Tensorflow | Regression | Deeplearning for Tabular Data | Spit->Iterate<->Switch

**Motivations**: 
      Ensemble Trees are great fit for classification but are not good conceptual fit for Regression problems.  
      Deeplearning models which ideally must be good fit still fails in case of tabular data.  
      Architecture of Tabular Deeplearning Models like Tabnet are not very intutive hence not beginner friendly.  

*Concept Contributors*: Rajesh Balakirshnan (rajeshbalakrishnan24@gmail.com)

*Concept Collaborators*: Looking for Collaborations | If you have developed any algorithm scratch you probably have good intution

*Code Collaborators*: Looking for Collaborations | You speak Python  

*Adoption Collaborators*: Looking for Collaborations | You have written medium post on a Machine learning Algorithm / posted atleast one video on AI/ML

Data might contain subgroups which might behave differently from each other hence might useful to split them up and train seperately"
As the name suggests switcher main idea is that it iteratively switches observations to respective best learner .

Switcher makes an attempts to make deeplearning work for tabular data. Its being built considering both beginner's ease of use and customisabliltity for advance user.

**Architecture**: Switchers architecture choice revolves around Split, Iterate and Switch functions.

**Train Cycle**:  Split Data (unsupervised ) -> Repeat( Iterative Regression like Deep ANN) per Split <-> Switch observation to respective best learner ) <- Best Learner Classifier

**Test Cycle** :  Best Learner Classifier -> Regressor 

**Results** : In progress. Will be reported soon. Initial test indicated significant improvement on regression tasks compared to vanilla Deep ANN. 








    

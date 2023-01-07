# Electric-Motor-temperature-prediction

![image](https://user-images.githubusercontent.com/105945382/211165188-76df35a2-2b0c-4e7b-92a5-604c0ba70686.png)

Electric motor is a device which is used to transform mechanical energy into electrical energy.
The principle of the electric motor involves the process of interaction between the
electric and magnetic fields, and the motion of the coil results in increase of temperature.
Elevated temperatures may cause insulation in the winding wires, which may result in short
circuits or causing the motor winding to burn out.
Considering temperature as the primary factor affecting the performance of an electric
motor, it is of utmost importance that an efficient mechanism is proposed for this
purpose. With an increase in the motor temperature, the resistance increases and the
torque constant and voltage constant decreases. Motor winding resistance is the key
reason behind heat generation within the motor. Using machine learning proves to be
significant as firstly, performing testing at initial stage results in prevention of damage to
the motors, thereby identifying the perfect temperature intervals for the electric motors to
work. Moreover the appropriate machine learning models assist in observing the areas
where modification pertaining to the motors is required.

## Following flow chart was used in this project:

<p align="center">
<img width="334" alt="image" src="https://user-images.githubusercontent.com/105945382/211165448-8069ca1e-d5d7-4543-b8b5-e35271b7b416.png">
</p>

<hr>

*Tools used*

- Python 
* HTML
+ Google Colab
- Flask
* IBM Cloud

<hr>

*Our dataset consists of 1000 rows with 13 attributes.*

***We collected our dataset from [kaggle](https://www.kaggle.com/datasets/wkirgsn/electric-motor-temperature)***

<sub>Following table consist of different attributes of the dataset:</sub>

|  u_q | coolant | stator_winding | i_q |
| :---: | :---: | :---: | :---: |
| u_d | motor_speed | pm | stator_yoke |
| stator_tooth  | i_d | ambient | torque |
| profile_id |

where, : 

- u_q : (Voltage q-component measurement)
* u_d : (Voltage d-component measurement)
+ i_d : (Current d-component measurement)
- i_q : (Current q-component measurement)
* pm : (Permanent magnet temperature)

<hr>

### Following models were used in this project

- Linear Regression
* Decision Tree
+ Random Forest
- Support Vector machine

<hr>

We built a web application that is integrated into the model we built. A UI is provided for the uses where he has to enter the values for predictions. The enter values are given to the saved model and prediction is showcased on the UI.


## Building The Python Flask App

We built our web application on python flask app (Flask is used for developing web applications using python)

*In the flask application, the user values are taken from the HTML page:*

![image](https://user-images.githubusercontent.com/105945382/211164655-bed747aa-a26f-4ef1-a268-773bb4906ba7.png)

*Load the home page:*

![image](https://user-images.githubusercontent.com/105945382/211164779-6814cada-17ca-4ed2-b1e8-a1fc48f6b12c.png)

*Prediction Function:*

![image](https://user-images.githubusercontent.com/105945382/211164852-e5d91d6e-4a65-49e8-b81e-2fe128ab1953.png)

<hr>

## Build An HTML Page 


We Build an HTML page to take the values from the user in a form and upon clicking on the predict button we get the temperature predicted. The values predicted are normalized values according to the dataset.

*This is how the home html page looks like where we will be entering our values to get the prediction:*

![image](https://user-images.githubusercontent.com/105945382/211164978-b6df2465-7d6a-48d7-bd3e-2abb3a5384cb.png)
 

### Now we integrate it into IBM 

At the final stage, the model was trained on IBM Watson and then deployed on IBM cloud.

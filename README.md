<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!--  -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!--
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  </a>


  <h1 align="center">Customer Churn Prediction System</h1>


  <p align="center">
    This is a simple Machine Learning model to predict whether the bank customer would churn or not !!   
  </p>
</p>

![Screenshot (189)](https://user-images.githubusercontent.com/75406889/122982686-c9527680-d3b8-11eb-8742-9da0919d9307.png)


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#approach">Approach</a></li>
    <!--
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Churn Prediction is an essential business metric which is adopted by various companies to analyse customer values and develop strategic marketing programs.It is also essential for banks ,
to decide , whether the customer would churn in the end or not. Due to the competitive atmosphere within electronic banking services , churn prediction is imperitive for customer retention.

### Built With

The prediction is based on Machine Learning Algorithms like Logistics Regression , Decision Tree and Random Forest , to get the best accuracy from the training data set.
I have deployed the model using Flask API in the backend.

<!-- USAGE EXAMPLES -->
## Usage

Here's how the Churn Prediction System works !!!

**Procedure for running the web app:**

Download all the files in the repository.Transfer these files ('app.py','templates','static', Churn_Prediction_Model.pkl') to your python directory. Run the file app.py in the python command line. Finally,the web application runs on your localhost, on your default web browser.

![Screenshot (179)](https://user-images.githubusercontent.com/75406889/122975215-bfc51080-d3b0-11eb-9dfa-1379ad38eb6d.png)
![Screenshot (180)](https://user-images.githubusercontent.com/75406889/122975228-c489c480-d3b0-11eb-854a-80012e0f1d77.png)
![Screenshot (181)](https://user-images.githubusercontent.com/75406889/122975244-c8b5e200-d3b0-11eb-9187-b824f75dfb1d.png)
![Screenshot (185)](https://user-images.githubusercontent.com/75406889/122975260-cc496900-d3b0-11eb-95ca-ee03a594e9d8.png)
![Screenshot (186)](https://user-images.githubusercontent.com/75406889/122975273-cfdcf000-d3b0-11eb-85ee-6b67434aafb1.png)
![Screenshot (190)](https://user-images.githubusercontent.com/75406889/122983616-d1f77c80-d3b9-11eb-8f24-210a38ffc48a.png)



<!--Approach-->
## Approach

The original dataset consists of 20 different features , that can be analysed to determine the churn status of the customer. These features include : 
* **Demographic Information** like Customer Id , Vintage -(of the customer with bank in days) , age , gender , dependents , occupation and city of the customer.

* **Customer-Bank Information** like Net worth (1-high , 2-low , 3-medium) , Branch Id and the Date of last transaction. 
* **Transactional Information** like Current Balance , Previous Month End Balance , Average Monthly Balance in Previous Quarter , Average Monthly Balance Previous to Previous Quarter
, Credit Amount current month , Credit Amount previous month , Debit Amount current month , Debit Amount previous month , Average Balance of current mont and Average Balance of previous month 


The final feature is Churn which we have to predict. This feature indicates 0 when the average balance of the customer falls below minimum in the next quarter , otherwise it is 1.

In the data preprocessing part , all the features are changed into either numerical or categorical type. The __*Date of last transaction*__ feature is used to extract other features like
the year or month or week or day of last transaction to realize clearly which time is more likely for a customer carry out transactions. Then univariate and bivariate analysis of all 
the features are carried out. Outliers and missing values are treated are as well.

Finally the dataset is splitted into training and test data and normalized using MinMaxScaler of the sklearn library. Applying **Logistic Regression** algorithm , 
gave an accuracy of **82.387%** on training data and **82.793%** on test data.

Next , I have applied **Decision Tree Classifier** along with 5-fold stratified cross validation.The mean accuracy obtained is 78.842%. The accuracy score obtained is lesser. 
So I have *tuned* some *hyperparameters* like *criterion , max_depth , max_features , max_leaf_nodes , min_samples_split* and *min_sample_leaf* using RandomizedSearchCV to get an accuracy
of **83.285%**.

The final model is based on **Random Forest Classifier** in addition to tuning hyperparameters like n_estimators , max_features , max_depth , min_samples_split and bootstrap using
RandomizedSearchCV. This model has an accuracy of **95.556%** on training data and **86.454%** on the test data.
Finally , I have saved the model in a .pkl file and deployed it using Flask API.

<!-- CONTRIBUTING 
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

-->

<!-- LICENSE 
## License

Distributed under the MIT License. See `LICENSE` for more information.

-->

<!-- CONTACT 
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)
-->


<!-- ACKNOWLEDGEMENTS 
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)

-->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png

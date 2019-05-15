+++
title = "Symptom Knowledge in Parkinson's Disease"
date = 2019-01-30T20:11:27+01:00
draft = false

authors = ["Julio Vega", "Caroline Jay", "Markel Vigo", "Simon Harper"]

# Tags: can be used for filtering projects.
# Example: `tags = ["machine-learning", "deep-learning"]`
tags = ["Parkinson's", "behaviour modelling", "Digital Health"]

# Project summary to display on homepage.
summary = "Personalised, unobtrusive and longitudinal monitoring of Parkinson's Disease symptom fluctions using smartphone data"

# Slides (optional).
#   Associate this page with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references 
#   `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides = ""

# Optional external URL for project (replaces project detail page).
external_link = ""

# Links (optional).
url_pdf = ""
url_code = ""
url_dataset = ""
url_slides = ""
url_video = ""
url_poster = "https://www.researchgate.net/publication/327537338_Personalised_Monitoring_of_Parkinson's_Disease_Using_Smartphones_and_Human_Behaviour"

# Custom links (optional).
#   Uncomment line below to enable. For multiple links, use the form `[{...}, {...}, {...}]`.
# links = [{icon_pack = "fab", icon="twitter", name="Follow", url = "https://twitter.com"}]

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
[image]
  # Caption (optional)
  caption = "SKIP's logo"

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = "Center"
+++

**Parkinson's Disease is a neurodegenerative condition with no cure and a wide variety of idiosyncratic motor and non-motor symptoms that impact people's quality of life.** In infrequent and short clinical consultations, health care professionals use validated clinical scales that are time-consuming and rely on clinical expertise or patients' perception. Moreover, symptoms can fluctuate within or between days due to the natural progression of the disease or medication and thus, a short session only provides a snapshot and not a longitudinal image of the disease. In practice, it is difficult for clinicians to tailor treatments and medication to each person's symptoms. Therefore, a granular, continuous, and objective methodology to track symptom fluctuations would improve patients' quality of life and make health services more efficient.

The complexity of Parkinson's makes it a challenging but suitable study case to investigate new personalised approaches supported by technology and tailored to each patient's condition. This work aims to explore the use of behavioural inferences extracted from smartphone data to track the fluctuations in Parkinson's Disease symptoms. **We recruited 7 participants with early Parkinson's (Hoehn \& Yahr scale <= 3), instrumented their personal Android and iOS mobiles, and collected a dataset with up to 22 data sources, 24/7, during 222 to 380 days and within the technological, ethical, and UX limitations of a real-world deployment**. As part of this dataset, we assessed their symptom severity using four clinical scales and seven cognitive tests every six weeks and patients self-reported the severity of their three main symptoms on a daily basis. 

Through an agile iterative design process, **we generated knowledge that supports ground truth collection for longitudinal Parkinson's tracking**. We identified five design implications for future Parkinson's self-reporting tools.  We published PaperStream, an open-source tool to create and encode questionnaires or surveys automatically. Also, we created a paper diary that blends digital and analogue data collection which participants used to gather daily self-reported symptom severity scores with average answer compliance of 96.39% (SD=0.05) among 7 participants monitored between 222 and 380 days.

**We created an adaptative method to track weekly self-reported fluctuations in pain, gait and fatigue, the first one of its kind for Parkinson's Precision Medicine**. Our method adapts to an individual's condition (personalised) and tracks symptoms while participants carry on with their regular lives (naturalistic), over time (longitudinal) and without people's input (unobtrusive). Instead of relying on the structure of the collected smartphone data to find patterns, our method starts with a generalised set of predictions based on mobility and activity recognition features that are overfitted to each patient's symptoms. We showed that this method tracks fluctuations better than chance with an agreement measured by Cohen's kappa between 0.19 and 0.53 finding a different subset of predictions for each participant. Also, exploring how this method can be deployed in the real world, we show that splitting our dataset into personalisation/testing sets is not a suitable strategy to identify a relevant subset of smartphone features to track symptoms on unseen data. 

Our results should be considered under the assumptions we made when we designed our method as well as the three primary sources of error in our methodology: the validity of the smartphone features, the confounders in participants behaviour, and the drawbacks of self-reporting. Nonetheless, this work is evidence that the unobtrusive and personalised monitoring methodology we proposed has the potential to track fluctuations in Parkinson's symptoms with the most impact on patients' daily life. Thus, we encourage researchers to tackle questions that remain open: how can we refine the mobility and activity recognition smartphone features we used? What other behavioural areas and smartphone features can be exploited to monitor other motor and non-motor symptoms? What other ground truth collection methods can minimise the problems related to analogue self-reported data? What is the clinical and self-management utility of the weekly fluctuations we tracked with our personalised models? What parameters and models of our method can be improved? Moreover, in the future, how can we include people with Parkinson's in the development and evaluation of their personalised models?
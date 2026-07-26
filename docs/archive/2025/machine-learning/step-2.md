---
layout: default
title: "Step 2 - Train the ML Model"
parent: "Machine Learning Introduction"
redirect_from:
  - "/part 3 tiny sorter/step-2.html"
---

# Step 2 - Train the ML Model

## What is Google Teachable Machine?


 In this step, you'll see how to train a computer to tell objects apart—using nothing but your webcam and a website, no programming required!  

{:.highlight}
We use [Google Teachable Machine](https://teachablemachine.withgoogle.com/), a free, web-based tool that lets anyone — even if you’ve never coded before — teach a machine learning (ML) model to recognize objects, sounds, or poses.

{:.highlight}
Under the hood, Teachable Machine uses a simplified version of **[TensorFlow.js](https://www.tensorflow.org/js)**, a technology for running machine learning directly in your browser.

**What’s a “machine learning model”?**  
 It’s like a super-powerful sorting rule. You show the computer lots of examples (e.g., photos of Block A, Block B …), and it “learns” how to tell them apart. Afterwards it can say things like: “I’m 95% sure this is Block A!”  

 In this workshop, our ML model looks at your webcam feed, decides which object it “sees,” and then sends that info to the Tiny Sorter for action.

{:.highlight}
If you're new to ML and interested, you can read this [beginner’s guide](https://developers.google.com/machine-learning/crash-course/ml-intro) to explore the main ideas. But you do not have to!

{:.highlight}
For the extra curious: Our model uses a so-called **neural network**, trained in real-time and run using JavaScript in the browser. Learn more about [neural nets](https://en.wikipedia.org/wiki/Artificial_neural_network).

---

## Step-by-Step Guide: Training Your Model

Below you'll find the main steps for training your Tiny Sorter ML model with Teachable Machine. For each part, watch the video or view the image, then follow the instructions.

---

### 1. Create a new Teachable Machine Project

- Go to [https://teachablemachine.withgoogle.com/](https://teachablemachine.withgoogle.com/).
- Click on **“Get Started”**, then **“Image Project”**, and choose **“Standard Image Model”**.
  
<div>
  <video autoplay muted loop playsinline title="TM Video 1" style="max-width: 100%; height: auto;">
    <source src="./assets/TM_video1.mov" type="video/quicktime">
  </video>
</div>

---

### 2. Set Up Your Classes

- You’ll see two default “classes”—rename them to match your object types, e.g., "Item A” and “Item B”.
- For our Tiny Sorter you have to created a third Class, e.g. "No Item", which we will use to train the model to recognize situations when there is no item to be sorted.

<div>
  <video autoplay muted loop playsinline title="TM Video 2" style="max-width: 100%; height: auto;">
    <source src="./assets/TM_video2.mov" type="video/quicktime">
  </video>
</div>

---

### 3. Record Training Data

- For each class, use your webcam to **capture at least 50 images**.
- Vary the angle, lighting, and distance as much as possible for best results!
- Move the object around to help the computer “see” it in different positions and conditions. This works best if you upload and start the provided code to the Pico beacuse there is an idle movement from left to right. 

<div>
  <video autoplay muted loop playsinline title="TM Video 3" style="max-width: 100%; height: auto;">
    <source src="./assets/TM_video3.mov" type="video/quicktime">
  </video>
</div>

{:.highlight}
As you can see in the video from the original Google project, they used Marshmallows and Cereals as their two Classes. 

<div>
  <video autoplay muted loop playsinline title="TM Video 4" style="max-width: 100%; height: auto;">
    <source src="./assets/TM_video4.mov" type="video/quicktime">
  </video>
</div>

{:.highlight}
Remember to also train a third class with nothing in it (this class will ensure that your sorter runs).

---

### 4. Train Your Model

- Click the **“Train Model”** button.
- Your browser will process the images and build a lightweight neural network behind the scenes.
- When done, you’ll see a live preview — insert up an object and watch the model try to classify it.

<div>
  <video autoplay muted loop playsinline title="TM Video 5" style="max-width: 100%; height: auto;">
    <source src="./assets/TM_video5.mov" type="video/quicktime">
  </video>
</div>

---

### 5. Export/Use the Model

- After training, go to the **“Export Model”** area.
- Choose **“Upload my model”** (makes it available online).
- Copy the provided **model link** to use with our sorting interface (you’ll need it later in Step 3).

<div>
  <video autoplay muted loop playsinline title="TM Video 6" style="max-width: 100%; height: auto;">
    <source src="./assets/TM_video6.mov" type="video/quicktime">
  </video>
</div>

---

## Next Step

Your model is now trained! Test it with your webcam before moving to the next step: setting up the electronics and connecting the Pi Pico.

[Continue with step 3 to get everything set up!](step-3){: .btn .btn-blue }.
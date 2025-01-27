# Fun Socks Box

Fun Socks Box is a B2C (business to customer) e-commerce site that focuses primarily on a monthly subscription service delivering a box of three unique socks each month to subscribed registered customers. There is also an option for any customer to purchase the socks individually or all three as a gift box, though this is more expensive per sock than the monthly subscription cost, plus free delivery is only available for 3 socks or more. 

According to the online e-commerce platform Shopify in their blog article titled ‘20 Trending Products and Things to Sell Online (2024)’ found [here](https://www.shopify.com/uk/blog/trending-products?term=&adid=595096101745&campaignid=17075828612&utm_medium=cpc&utm_source=google&gad_source=1&gclid=EAIaIQobChMInsKR2qKfiQMV36BaBR2QEi4gEAAYASAAEgKmivD_BwE&cmadid=516586848;cmadvertiserid=10730501;cmcampaignid=26990768;cmplacementid=324286430;cmcreativeid=163722649;cmsiteid=5500011#10), listing the top 20 trending products sold by US Shopify merchants, socks are simple yet profitable choice for e-commerce brands. It also states that socks are a popular choice for subscription boxes.

[Link to the live website](https://mwbark-funsocksbox-6de564e8a4a8.herokuapp.com/)

## Planning

<details>

<summary>The Database Schema used for this project</summary>

![Entity Relationship Diagram](documentation/erd.jpeg)
</details>
<BR>
<details>

<summary>Wireframes</summary>

<br>

[Desktop Wireframes pdf](documentation/wireframes-desktop.pdf)
</details>

### Agile Methodology

Github Issues were used to create User Stories to plan actions to take in the project. Issues contained acceptance criteria to guide me in creating features and knowing when they were completed.

5 issues from the back catalog, with MoSCoW 'must have' ranking or highest available, were then put into a sprint/milestone to create a project iteration. Within the sprint, 3 issues (60%) were labeled 'must have' while the other 2 were labeled 'should have' or 'could have'.

The issues from the sprint were then added to a 'Fun Socks Box' Project board 'Todo' column. Issues were then, by priority, moved to the 'In Progress' and then 'Done' coloumn on completion. Any issues not completed before the sprint/iteration deadline were added back to the back catalog for reprioritisation.

## Features

### Existing features

**Header & Navigation**

- Site name and logo redirects to home page.

- ‘Subscribe’ and ‘Products’ link to related pages.

- On smaller screen sizes ‘Home’, ‘Subscribe’ and ‘Products’ are contained in a dropdown from a burger button.

- ‘My Account’ triggers a dropdown where users who haven't logged in can navigate to login and signup pages and logged in users can navigate to their ‘Address Book’ page, a logout page and a portal to Stripe to manage their subscription if they have one.

- The bag icon links to the bag page and the price icon shows the grand total of the user’s current bag.

- A banner alerts the user to the free delivery threshold.

**Home**

- An opaque card contains a description with site keywords relating to socks subscription box. A button links to the subscription page.

- Another card contains the call to sign up to the site’s newsletter via Intuit Mailchimp.

**Subscription**

- A card contains pricing and details relating to the monthly subscription box as well as a link to Stripe to subscribe.

**Products**

- Cards show images and names of this month's socks products and link to related sock product when clicked.

- Admin can see buttons to delete individual products and an ‘Add Product’ button to add a product.

**Product Detail**

- Slideshow of all related product images.

- Name, description and price of product.

- Buttons to select size any quantity when added to bag.

- Buttons to 'Add to Bag' and 'Keep Shopping'.

- Admin can 'Manage Images' and 'Update Product'.

### Future features

## Testing

## Bugs

### Fixed

### Remaining

## Deployment

## Credits

### Code

### Media

## Acknowledgements

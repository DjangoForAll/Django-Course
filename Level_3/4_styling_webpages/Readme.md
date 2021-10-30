Lets also take a quick refresher on styling web pages.

CSS is a language that allows us to style our html page. CSS was designed to seperate the styling of our html page from the html content itself. This means that we can reuse the css designs for multiple pages. The seperation of styles and content allows the same page to behave differently based on how the page is being viewed, such as if the page is being viewed in a mobile device, a desktop device, if the page is being printed or even if it is read by a voice over tool.

A Quick Example of an inline css style is below:

```html
<h1 style="color:red">Text in Red Color</h1>
<h1 style="font-size: 1.2em;color:red">Huge Text in Red Color</h1>
```

This is the hacky way to add styles to out elements. This method is not reccomended since these styles cannot be reused by any other element.

The better way to add styles is to create style classes and then add them to our elements. Style classes can be defined in a seperate standalone css file or within the html document itself

An Example with CSS Classes can be:

```html
<style>
  .red {
    color: red;
  }
  .big {
    font-size: 10em;
  }
</style>

<h1 class="red">Text in Red Color</h1>
<h1 class="red big">Huge Text in Red Color</h1>
```

In this example we have defined two classes, red and big. We then added the class to our html elements.

If you observe the above example, the class red was only defined once but was used in two elements, HTML elements support multiple classes so we can easily combine different classes to create the desired styling effect.

In the above example we used styling within the html docuement itself. This is not reccomended since it is not possible to reuse the style classes in other html documents. This is why we usually use a seperate css file.

To create seperate css files we use the following syntax:

```html
<link rel="stylesheet" href="style.css" />
```

This element is added to the head of the html document, This is not mandatory, but is reccomended.

CSS Stands for Cascading Style Sheets, Its called cascading because the style is applied on a priority basis, the style from the stylesheet gets the least priority while the inline style gets the highest priority, that way you can override changes if needed.

To take a look at all the valid CSS properties, Visit this [page](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#index)

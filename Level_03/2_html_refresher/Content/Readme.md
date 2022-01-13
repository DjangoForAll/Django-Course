let's Refresh our HTML Skills,

### HTML (_Hyper Text Markup Language_)

Html is a markup language that is used to describe the structure of a webpage.

Markup languages are composed of tags and attributes. HTML is more human-readable compared to other languages, they cannot be used to create logical programs, they can only store the structure of the web page.

We'll just focus only on the basics for now.

### Tags and Attributes

Tags are used to hold elements in an HTML document. Tags can have attributes that are used to describe the element.

HTML Tags start with a `<` and end with a `>`. Most HTML elements have a start tag and a closing tag.

A sample tag that holds some content will look like this

```html
<ExampleTag attribute="Value"> Content </ExampleTag>
```

You can nest tags in order to create more complex elements. Note that when you nest tags the tag that was opened last should be closed first. Note that attributes are added in the opening tag only.

```html
<ExammpleTag1>
    <ExampleTag2>
        Content
    </ExampleTag2>
</ExampleTag1>
```

HTML has a predefined standard set of tags. These tags help design our web pages.  
Some examples are:

```html
<h1 align="center">This is the Largest Heading</h1>
```

Here `h1` is the tag for the largest heading. The content is between the tags. `align` is an attribute that is used to align the content. `center` is the value of the attribute align.

Html provides a lot of standard tags for building web pages.  
You can visit the following link to see a list of all the tags and how they can be used

[MDN Mozilla Html Reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

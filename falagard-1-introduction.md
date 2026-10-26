<a id="fal_intro"></a>
# Introduction and overview

> CEGUI 0.8.7 · Falagard skinning system · converted from [`fal_intro.dox`](https://github.com/cegui/cegui/blob/v0-8-7/doc/doxygen/falagard/fal_intro.dox) ([original page](https://static.cegui.org.uk/docs/0.8.7/fal_intro.html)). Text unchanged; format only.

<a id="fal_whatis"></a>
## What is the Falagard Skinning System?

The Falagard skinning system for CEGUI consists partly of a set of enhancements to the CEGUI base library, and partly of a window renderer module called "CEGUICoreWindowRendererSet". Combined, these elements are intended to make it easier to create custom skins or 'looks' for CEGUI window and widget elements.

The Falagard system is designed to allow widget imagery specification, sub-widget layout, and default property initialisers to be specified via XML files rather than in C++ or scripted code (which, before now, was the only way to do these things).

The system is named "Falagard" after the forum name of the person who initially suggested the feature (as is the trend in all things CEGUI), although it was designed and implemented by the core CEGUI team.

The Falagard extensions are not limited to the 'looknfeel' XML files only; there are supporting elements within the core library, as well as extensions to the GUI scheme system to allow you to create what are essentially new widget types. This is achieved by mapping a named widget 'look' and a named window renderer to a named widget base type.  I've probably just about lost you now, the best thing is to not worry about all these details for the time being!

Once your new type has been defined in a scheme and loaded, you can specify the name of that new type name when creating windows or widgets via the WindowManager singleton as you would for any other widget type. There are no additional issues to be considered when using a 'skinned' widget than when using one of the old 'programmed' widget types.

<a id="fal_intro_contents"></a>
## Section Contents

- [The Unified Co-ordinate System](#fal_unifiedsystem)
- [The UDim type](#fal_udim)
- [The UVector2 type](#fal_uvector2)
- [The URect type](#fal_urect)
- [Window Alignments](#fal_window_alignments)
- [Falagard in Schemes](#fal_schemes)
- [Conclusion](#fal_conclusion)

<a id="fal_unifiedsystem"></a>
## The Unified Co-ordinate System

As part of the Falagard system, CEGUI has effectively replaced the old either/or approach to relative and absolute co-ordinates with a new 'unified' co-ordinate system. Using this new system, each co-ordinate can specify both a parent-relative and absolute-pixel component. Since most people baulk at the idea of this, I'll use examples to introduce these concepts.

<a id="fal_udim"></a>
### UDim

<a id="fal_udim_def"></a>
#### UDim Definition

The basic building block of the unified system is the UDim. This type represents a single dimension of some kind, and is defined as:

```cpp
UDim(scale, offset)
```

where:

- `scale` represents some proportion of the parent element, where the parent element is either some other Window or the total available display, and is usually a value between 0 and 1.0. The scale value corresponds to relative coordinates under the pre-unified system.
- `offset` represents an arbitrary number of pixels. For positional values, offset represents a pixel offset, for size values, offset represents a number of additional pixels (basically like a padding value).  The offset value corresponds to absolute coordinates under the pre-unified system.

Still confused? On to the examples!

<a id="fal_udim_examples"></a>
#### Simple UDim Examples

<a id="fal_udim_example1"></a>
##### Example 1

```cpp
UDim(0, 10)
```

Here we see a UDim with a scale of 0, and an offset of 10. This simply represents an absolute value of 10, if you used such a UDim to set a window width, then under the old system it's the equivalent of:

```cpp
myWindow->setWidth(Absolute, 10);
```

<a id="fal_udim_example2"></a>
##### Example 2

```cpp
UDim(0.25f, 0)
```

Here we see a UDim with a scale of 0.25 and an offset of 0. This represents a simple relative co-ordinate. If you were to set the y position of a window using this UDim, then the window would be a quarter of the way down it's parent, and it's the same as the following under the old system:

```cpp
myWindow->setYPosition(Relative, 0.25f);
```

<a id="fal_udim_example3"></a>
##### Example 3

```cpp
UDim(0.33f, -15)
```

Here we see the power of UDim. We have a scale of 0.33 and an offset of -15. If we used this as the height of a window, you would get a height that is approximately one third of the height of the window's parent, minus 15 pixels. There is no simple equivalent for this under the old system.

<a id="fal_udim_prop_fmt"></a>
#### UDim Property Format

The format of a UDim to be used in the window property strings is as follows:

```text
{s,o}
```

where:

- `s` is the scale value.
- `o` is the pixel offset.

<a id="fal_uvector2"></a>
### UVector2

<a id="fal_uvector2_def"></a>
#### UVector2 Definition

There is a UVector2 type which consists of two UDim elements; one for the x axis, and one for the y axis. Note that the UVector2 is used to specify both positional points and also sizes; that is, there is no such thing as USize to correspond to the CEGUI::Size type that used to be used for specifying a size.

The UVector2 is defined as:

```cpp
UVector2(x_udim, y_udim)
```

where:

- `x_udim` is a UDim value that specifies the x co-ordinate or width.
- `y_udim` is a UDim value that specifies the y co-ordinate or height.

<a id="fal_uvector2_examples"></a>
#### Simple UVector2 Examples

<a id="fal_uvec2_example1"></a>
##### Example 1

```cpp
UVector2( UDim(0, 25), UDim(0.2f, 12) )
```

The above example specifies a point that is 25 pixels along the x-axis and one fifth of the way down the parent window plus twelve pixels.

<a id="fal_uvec2_example2"></a>
##### Example 2

```cpp
UVector2( UDim(1.0f, -25), UDim(1.0f, -25) )
```

This example, intended as a size for a window, would give the window the same width as its parent, minus 25 pixels, and the same height as its parent, minus 25 pixels.

<a id="fal_uvector2_prop_fmt"></a>
#### UVector2 Property Format

The format of a UVector2 to be used in the window property strings is as follows:

```text
{{sx,ox},{sy,oy}}
```

where:

- `sx` is the scale value for the x-axis
- `ox` is the pixel offset for the x-axis.
- `sy` is the scale value for the y-axis
- `oy` is the pixel offset for the y-axis.

<a id="fal_urect"></a>
### URect

<a id="fal_urect_def"></a>
#### URect Definition

The last of the Unified co-ordinate types is URect. The URect defines four sides of a rectangle using UDim elements. You generally access the URect as you would the normal 'Rect' type, except that each edge of the rectangle is represented by a UDim rather than a float, or any other type you may be used to seeing!

```cpp
URect(left_udim, top_udim, right_udim, bottom_udim)
```

where:

- `left_udim` is a UDim defining the left edge.
- `top_udim` is a UDim defining the top edge.
- `right_udim` is a UDim defining the right edge.
- `bottom_udim` is a UDim defining the bottom edge.

It is also possible to define a URect with two UVector2 objects; the first describes the top-left corner, and the second the bottom-right corner:

```cpp
URect(tl_uvec2, br_uvec2)
```

where:

- `tl_uvec2` is a UVector2 that describes the top-left point of the rect area.
- `br_uvec2` is a UVector2 that describes the bottom-right point of the rect area.  Don't confuse this with the size of the area.

<a id="fal_urect_examples"></a>
#### Simple URect Example

```cpp
URect( UDim(0, 25),
       UDim(0, 25),
       UDim(1.0f, -25),
       UDim(1.0f, -25)
     )
```

If we used the URect defined here to specify the area for a window, we would get a window that was 25 pixels smaller than its parent on each edge.

<a id="fal_urect_prop_fmt"></a>
#### URect Property format

The format of a URect to be used in the window property strings is as follows:

```text
{{sl,ol},{st,ot},{sr,or},{sb,ob}}
```

where:

- `sl` is the scale value for the left edge.
- `ol` is the pixel offset for the left edge.
- `st` is the scale value for the top edge.
- `ot` is the pixel offset for the top edge.
- `sr` is the scale value for the right edge.
- `or` is the pixel offset for the right edge.
- `sb` is the scale value for the bottom edge.
- `ob` is the pixel offset for the bottom edge.

<a id="fal_window_alignments"></a>
## Window Alignments

The Falagard enhancements also include settings to specify alignments for windows. This gives the possibility to position child windows from the right edge, bottom edge and centre positions of their parents, as well as the previous left edge and top edge possibilities.

It is possible to set the alignment options in C++ code by using methods in the Window class, and also via the properties system which is used by XML layouts system.

<a id="fal_vert_alignments"></a>
### Vertical Alignments

To set the vertical alignment use the Window class member function:

```cpp
void setVerticalAlignment(const VerticalAlignment alignment);
```

This function takes one of the VerticalAlignment enumerated values as its input. The VerticalAlignment enumeration is defined as:

```cpp
enum VerticalAlignment
{
    VA_TOP,
    VA_CENTRE,
    VA_BOTTOM
};
```

Where:

- `VA_TOP` specifies that y-axis positions specify an offset for a window's top edge from the top edge of it's parent window.
- `VA_CENTRE` specifies that y-axis positions specify an offset for a window's centre point from the centre point of it's parent window.
- `VA_BOTTOM` specifies that y-axis positions specify an offset for a window's bottom edge from the bottom edge of it's parent window.

The window property to access the vertical alignment setting is:

```text
"VerticalAlignment"
```

This property takes a simple string as its value, which should be one of the following options:

```text
"Top"
"Centre"
"Bottom"
```

Where these setting values correspond to the similar values in the VerticalAlignment enumeration.

<a id="fal_horz_alignments"></a>
### Horizontal Alignments

To set the horizontal alignment use the Window class member function:

```cpp
void setHorizontalAlignment(const HorizontalAlignment alignment);
```

This function takes one of the HorizontalAlignment enumerated values as its input. The HorizontalAlignment enumeration is defined as:

```cpp
enum HorizontalAlignment
{
    HA_LEFT,
    HA_CENTRE,
    HA_RIGHT
};
```

Where:

- `HA_LEFT` specifies that x-axis positions specify an offset for a window's left edge from the left edge of it's parent window.
- `HA_CENTRE` specifies that x-axis positions specify an offset for a window's centre point from the centre point of it's parent window.
- `HA_RIGHT` specifies that x-axis positions specify an offset for a window's right edge from the right edge of it's parent window.

The window property to access the horizontal alignment setting is:

```text
"HorizontalAlignment"
```

This property takes a simple string as its value, which should be one of the following options:

```text
"Left"
"Centre"
"Right"
```

Where these setting values correspond to the similar values in the HorizontalAlignment enumeration.

<a id="fal_schemes"></a>
## Falagard in Schemes

The CEGUI scheme system is the means by which you to specify how the system is to load your XML skin definition files, known as 'looknfeel' files, and how these skins are to be mapped to window renderers and widget base classes to create new concrete widget types.

<a id="fal_wr_modules"></a>
### The CEGUICoreWindowRendererSet module

One of the main parts of the Falagard system is the window renderer module known as CEGUICoreWindowRendererSet (which will be named libCEGUICoreWindowRendererSet.so on linux style systems and CEGUICoreWindowRendererSet.dll on Win32 systems). This module contains a set of predefined window renderer classes that take actions to transform skinning data loaded from skin definition XML files into the rendering operations and layout adjustments required to output the widget visual representation to the display.

Before you can make use of the CEGUICoreWindowRendererSet module it must be loaded into the system. To achieve this, you will usually specify it in one of your scheme XML files so that it's available to the system.  This can be done with a single line of XML in a scheme file, such as:

```xml
<WindowRendererSet Filename="CEGUICoreWindowRendererSet" />
```

Some users, having previously employed the WindowSet 'look' modules, may be used to specifying a list of widgets which are to be made available from the module, this is not required when loading a WindowRenderer module (actually, such lists of widgets are no longer needed for the old style 'look' modules either, as long as the module has been updated to provide the required entry point); by employing XML such as that shown above, the module will register all widget types it has available.

The key thing about the CEGUICoreWindowRendererSet module is that for each widget base type, it defines various required elements and states.  These required items need to be defined within the widget look definitions of your looknfeel XML files; they enable the system to make use of your skin imagery and related data in a logical fashion. All of the required elements for each widget can be found in the reference sections [CEGUI Widget Base Type Requirements](falagard-5-base-type-requirements.md#fal_baseclass_ref) and [Falagard Window Renderer Requirements](falagard-6-window-renderer-requirements.md#fal_wr_ref).

<a id="fal_looknfeel_elements"></a>
### LookNFeel Elements

The `<LookNFeel>` XML element for schemes is the means by which you will usually get CEGUI to load the XML 'looknfeel' files containing your widget skin definitions.  It is possible to load these files manually via code, but it is expected that the majority of users will be using the scheme system. The LookNFeel element should appear after any Font or Imageset elements, but before any WindowSet elements.

The following is an example of how to use the LookNFeel element:

```xml
<LookNFeel Filename="FunkyWidgets.looknfeel" />
```

Here we can see a single 'Filename' attribute which specifies the name the file to be loaded.

It is acceptable to specify as many LookNFeel elements as is required.  This allows you to configure your XML files in the way that best suits your application. This might mean that all skin definitions for all widget elements will go into a single file, it might mean that you have multiple files with a single widget skin definition in each, or it could be any place in between the two extremes - it's up to you.

<a id="fal_mappings"></a>
### FalagardMapping Elements

The CEGUI scheme system supports a `<FalagardMapping>` element that creates a new concrete window or widget type within the system. This is achieved by creating a named alias that ties together a base widget type, a window renderer type, and a named widget 'LookNFeel'.  Here, 'LookNFeel' refers to an individual widget skin as opposed to an entire 'looknfeel' XML file.  The base widget type will generally be one of the core system widgets provided by the CEGUI library, although any window type that has a concrete WindowFactory registered in the system is a candidate, which allows the system to be extended with custom widgets.  The window renderer type will usually be the name of one of the window renderers registered when the CEGUICoreWindowRendererSet module was loaded, again this is not a requirement - the window renderer used could just as easily be one you have written yourself.  The named 'LookNFeel' is what you specify in your XML looknfeel files (via WidgetLook elements).

An example mapping:

```xml
<FalagardMapping
    WindowType="FunkyLook/Button"
    TargetType="CEGUI/PushButton"
    Renderer="Falagard/Button"
    LookNFeel="MyButtonSkin"
/>
```

In this example, a new widget type named "FunkyLook/Button" is being created. The new widget is based upon the "CEGUI/PushButton" base type, uses the window renderer named "Falagard/Button" and applies the skin defined by the loaded WidgetLook named "MyButtonSkin".  Once the scheme with this mapping has been loaded, you can then use the new type within the system:

```cpp
// Get access to the main window manager
CEGUI::WindowManager wMgr& = CEGUI::WindowManager::getSingleton();

// Create a new widget
Window* wnd = wMgr.createWindow("FunkyLook/Button", "myFunkyButton");
```

Here we create an instance of the new widget, and name it "myFunkyButton".  The widget can now be attached to other windows and generally used as you would any 'normal' widget.

<a id="fal_conclusion"></a>
## Conclusion

This concludes the overview of the new parts of the CEGUI system.

You have seen how the new unified coordinate system works, and how to make use of the new window alignment options.

You have also learned the basics of how to set up your scheme files to initialise the Falagard window renderer module, and how to map skins defined in XML files to the Falagard to create new widget types.

The next section of this document will introduce the XML format and elements used in the 'looknfeel' files.

---

Copyright (c) 2006 - 2011 Paul D Turner & The CEGUI Development Team

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.2
or any later version published by the Free Software Foundation; with
no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in [GNU-FDL-1.2.md](GNU-FDL-1.2.md).

*Modified version:* converted from the Doxygen sources of CEGUI 0.8.7 to Markdown.
Only formatting was changed; the text is the original.

Introduction
============

This is a full-blown functional test. The emphasis here is on testing what
the user may input and see, and the system is largely tested as a black box.
We use PloneTestCase to set up this test as well, so we have a full Plone site
to play with. We *can* inspect the state of the portal, e.g. using 
self.portal and self.folder, but it is often frowned upon since you are not
treating the system as a black box. Also, if you, for example, log in or set
roles using calls like self.setRoles(), these are not reflected in the test
browser, which runs as a separate session.

Being a doctest, we can tell a story here.

First, we must perform some setup. We use the testbrowser that is shipped
with Five, as this provides proper Zope 2 integration. Most of the 
documentation, though, is in the underlying zope.testbrower package.

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()

The following is useful when writing and debugging testbrowser tests. It lets
us see all error messages in the error_log.

    >>> self.portal.error_log._ignored_exceptions = ()

With that in place, we can go to the portal front page and log in. We will
do this using the default user from PloneTestCase:

    >>> from Products.PloneTestCase.setup import portal_owner, default_password

    >>> browser.open(portal_url)

We have the login portlet, so let's use that.

    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()

Here, we set the value of the fields on the login form and then simulate a
submit click.

We then test that we are still on the portal front page:

    >>> browser.url == portal_url
    True

And we ensure that we get the friendly logged-in message:

    >>> "You are now logged in" in browser.contents
    True


-*- extra stuff goes here -*-
The CarouselBlockImage content type
===============================

In this section we are tesing the CarouselBlockImage content type by performing
basic operations like adding, updadating and deleting CarouselBlockImage content
items.

Adding a new CarouselBlockImage content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'CarouselBlockImage' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CarouselBlockImage').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CarouselBlockImage' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CarouselBlockImage Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'CarouselBlockImage' content item to the portal.

Updating an existing CarouselBlockImage content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New CarouselBlockImage Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New CarouselBlockImage Sample' in browser.contents
    True

Removing a/an CarouselBlockImage content item
--------------------------------

If we go to the home page, we can see a tab with the 'New CarouselBlockImage
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New CarouselBlockImage Sample' in browser.contents
    True

Now we are going to delete the 'New CarouselBlockImage Sample' object. First we
go to the contents tab and select the 'New CarouselBlockImage Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New CarouselBlockImage Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New CarouselBlockImage
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New CarouselBlockImage Sample' in browser.contents
    False

Adding a new CarouselBlockImage content item as contributor
------------------------------------------------

Not only site managers are allowed to add CarouselBlockImage content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'CarouselBlockImage' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CarouselBlockImage').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CarouselBlockImage' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CarouselBlockImage Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new CarouselBlockImage content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The CarouselBanner content type
===============================

In this section we are tesing the CarouselBanner content type by performing
basic operations like adding, updadating and deleting CarouselBanner content
items.

Adding a new CarouselBanner content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'CarouselBanner' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CarouselBanner').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CarouselBanner' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CarouselBanner Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'CarouselBanner' content item to the portal.

Updating an existing CarouselBanner content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New CarouselBanner Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New CarouselBanner Sample' in browser.contents
    True

Removing a/an CarouselBanner content item
--------------------------------

If we go to the home page, we can see a tab with the 'New CarouselBanner
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New CarouselBanner Sample' in browser.contents
    True

Now we are going to delete the 'New CarouselBanner Sample' object. First we
go to the contents tab and select the 'New CarouselBanner Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New CarouselBanner Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New CarouselBanner
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New CarouselBanner Sample' in browser.contents
    False

Adding a new CarouselBanner content item as contributor
------------------------------------------------

Not only site managers are allowed to add CarouselBanner content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'CarouselBanner' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CarouselBanner').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CarouselBanner' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CarouselBanner Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new CarouselBanner content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The CarouselBlock content type
===============================

In this section we are tesing the CarouselBlock content type by performing
basic operations like adding, updadating and deleting CarouselBlock content
items.

Adding a new CarouselBlock content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'CarouselBlock' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CarouselBlock').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CarouselBlock' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CarouselBlock Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'CarouselBlock' content item to the portal.

Updating an existing CarouselBlock content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New CarouselBlock Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New CarouselBlock Sample' in browser.contents
    True

Removing a/an CarouselBlock content item
--------------------------------

If we go to the home page, we can see a tab with the 'New CarouselBlock
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New CarouselBlock Sample' in browser.contents
    True

Now we are going to delete the 'New CarouselBlock Sample' object. First we
go to the contents tab and select the 'New CarouselBlock Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New CarouselBlock Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New CarouselBlock
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New CarouselBlock Sample' in browser.contents
    False

Adding a new CarouselBlock content item as contributor
------------------------------------------------

Not only site managers are allowed to add CarouselBlock content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'CarouselBlock' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CarouselBlock').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CarouselBlock' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CarouselBlock Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new CarouselBlock content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The SplashBlock content type
===============================

In this section we are tesing the SplashBlock content type by performing
basic operations like adding, updadating and deleting SplashBlock content
items.

Adding a new SplashBlock content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'SplashBlock' and click the 'Add' button to get to the add form.

    >>> browser.getControl('SplashBlock').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'SplashBlock' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'SplashBlock Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'SplashBlock' content item to the portal.

Updating an existing SplashBlock content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New SplashBlock Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New SplashBlock Sample' in browser.contents
    True

Removing a/an SplashBlock content item
--------------------------------

If we go to the home page, we can see a tab with the 'New SplashBlock
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New SplashBlock Sample' in browser.contents
    True

Now we are going to delete the 'New SplashBlock Sample' object. First we
go to the contents tab and select the 'New SplashBlock Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New SplashBlock Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New SplashBlock
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New SplashBlock Sample' in browser.contents
    False

Adding a new SplashBlock content item as contributor
------------------------------------------------

Not only site managers are allowed to add SplashBlock content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'SplashBlock' and click the 'Add' button to get to the add form.

    >>> browser.getControl('SplashBlock').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'SplashBlock' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'SplashBlock Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new SplashBlock content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The ListingBlock content type
===============================

In this section we are tesing the ListingBlock content type by performing
basic operations like adding, updadating and deleting ListingBlock content
items.

Adding a new ListingBlock content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'ListingBlock' and click the 'Add' button to get to the add form.

    >>> browser.getControl('ListingBlock').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'ListingBlock' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'ListingBlock Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'ListingBlock' content item to the portal.

Updating an existing ListingBlock content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New ListingBlock Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New ListingBlock Sample' in browser.contents
    True

Removing a/an ListingBlock content item
--------------------------------

If we go to the home page, we can see a tab with the 'New ListingBlock
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New ListingBlock Sample' in browser.contents
    True

Now we are going to delete the 'New ListingBlock Sample' object. First we
go to the contents tab and select the 'New ListingBlock Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New ListingBlock Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New ListingBlock
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New ListingBlock Sample' in browser.contents
    False

Adding a new ListingBlock content item as contributor
------------------------------------------------

Not only site managers are allowed to add ListingBlock content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'ListingBlock' and click the 'Add' button to get to the add form.

    >>> browser.getControl('ListingBlock').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'ListingBlock' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'ListingBlock Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new ListingBlock content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The HighlightBlock content type
===============================

In this section we are tesing the HighlightBlock content type by performing
basic operations like adding, updadating and deleting HighlightBlock content
items.

Adding a new HighlightBlock content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'HighlightBlock' and click the 'Add' button to get to the add form.

    >>> browser.getControl('HighlightBlock').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'HighlightBlock' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'HighlightBlock Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'HighlightBlock' content item to the portal.

Updating an existing HighlightBlock content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New HighlightBlock Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New HighlightBlock Sample' in browser.contents
    True

Removing a/an HighlightBlock content item
--------------------------------

If we go to the home page, we can see a tab with the 'New HighlightBlock
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New HighlightBlock Sample' in browser.contents
    True

Now we are going to delete the 'New HighlightBlock Sample' object. First we
go to the contents tab and select the 'New HighlightBlock Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New HighlightBlock Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New HighlightBlock
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New HighlightBlock Sample' in browser.contents
    False

Adding a new HighlightBlock content item as contributor
------------------------------------------------

Not only site managers are allowed to add HighlightBlock content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'HighlightBlock' and click the 'Add' button to get to the add form.

    >>> browser.getControl('HighlightBlock').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'HighlightBlock' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'HighlightBlock Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new HighlightBlock content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The LandingPage content type
===============================

In this section we are tesing the LandingPage content type by performing
basic operations like adding, updadating and deleting LandingPage content
items.

Adding a new LandingPage content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'LandingPage' and click the 'Add' button to get to the add form.

    >>> browser.getControl('LandingPage').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'LandingPage' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'LandingPage Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'LandingPage' content item to the portal.

Updating an existing LandingPage content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New LandingPage Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New LandingPage Sample' in browser.contents
    True

Removing a/an LandingPage content item
--------------------------------

If we go to the home page, we can see a tab with the 'New LandingPage
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New LandingPage Sample' in browser.contents
    True

Now we are going to delete the 'New LandingPage Sample' object. First we
go to the contents tab and select the 'New LandingPage Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New LandingPage Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New LandingPage
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New LandingPage Sample' in browser.contents
    False

Adding a new LandingPage content item as contributor
------------------------------------------------

Not only site managers are allowed to add LandingPage content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'LandingPage' and click the 'Add' button to get to the add form.

    >>> browser.getControl('LandingPage').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'LandingPage' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'LandingPage Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new LandingPage content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The LittleBlock content type
===============================

In this section we are tesing the LittleBlock content type by performing
basic operations like adding, updadating and deleting LittleBlock content
items.

Adding a new LittleBlock content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'LittleBlock' and click the 'Add' button to get to the add form.

    >>> browser.getControl('LittleBlock').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'LittleBlock' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'LittleBlock Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'LittleBlock' content item to the portal.

Updating an existing LittleBlock content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New LittleBlock Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New LittleBlock Sample' in browser.contents
    True

Removing a/an LittleBlock content item
--------------------------------

If we go to the home page, we can see a tab with the 'New LittleBlock
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New LittleBlock Sample' in browser.contents
    True

Now we are going to delete the 'New LittleBlock Sample' object. First we
go to the contents tab and select the 'New LittleBlock Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New LittleBlock Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New LittleBlock
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New LittleBlock Sample' in browser.contents
    False

Adding a new LittleBlock content item as contributor
------------------------------------------------

Not only site managers are allowed to add LittleBlock content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'LittleBlock' and click the 'Add' button to get to the add form.

    >>> browser.getControl('LittleBlock').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'LittleBlock' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'LittleBlock Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new LittleBlock content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The BigBlock content type
===============================

In this section we are tesing the BigBlock content type by performing
basic operations like adding, updadating and deleting BigBlock content
items.

Adding a new BigBlock content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'BigBlock' and click the 'Add' button to get to the add form.

    >>> browser.getControl('BigBlock').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'BigBlock' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'BigBlock Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'BigBlock' content item to the portal.

Updating an existing BigBlock content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New BigBlock Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New BigBlock Sample' in browser.contents
    True

Removing a/an BigBlock content item
--------------------------------

If we go to the home page, we can see a tab with the 'New BigBlock
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New BigBlock Sample' in browser.contents
    True

Now we are going to delete the 'New BigBlock Sample' object. First we
go to the contents tab and select the 'New BigBlock Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New BigBlock Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New BigBlock
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New BigBlock Sample' in browser.contents
    False

Adding a new BigBlock content item as contributor
------------------------------------------------

Not only site managers are allowed to add BigBlock content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'BigBlock' and click the 'Add' button to get to the add form.

    >>> browser.getControl('BigBlock').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'BigBlock' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'BigBlock Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new BigBlock content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)




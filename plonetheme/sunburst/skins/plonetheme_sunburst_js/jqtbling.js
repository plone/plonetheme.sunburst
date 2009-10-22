/******
    Standard popups
******/
jq(function(){
    // login form
    jq('#portal-personaltools a[href$=/login]').prepOverlay(
        {
            subtype: 'ajax',
            filter: '#content>*',
            formselector: 'form#login_form',
            noform: 'reload'
        }
    );

    // delete / rename confirmation dialog;
    jq('#plone-contentmenu-actions a#delete, #plone-contentmenu-actions a#rename').prepOverlay(
        {
            subtype:'ajax',
            filter: '#content>*',
            closeselector: '[name=form.button.Cancel]'
        }
    );
});


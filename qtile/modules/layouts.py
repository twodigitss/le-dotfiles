from libqtile import layout
from libqtile.config import Match
from colorsheet import defs

layouts = [
    layout.Bsp(
        border_on_single=1,
        border_width = 0,
        margin_on_single=10,
        margin=5,
        border_focus=defs["egg"],
        border_normal=defs["unused"],
        lower_right=False, 
    ), 
    layout.Spiral( 
        border_focus=defs["coldwhite"],
        border_normal=defs["unused"],
        border_width = 0, margin=10,
        main_pane='right', clockwise=True,
        new_client_position='left',
    ),

]

floating_layout = layout.Floating(
    border_focus=defs["coldwhite"],
    border_normal=defs["coldwhite"],
    border_width = 0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

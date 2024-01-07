# Ivaylo Kuzev <ivkuzev@gmail.com>, 2014
# Zenburn like colorscheme for https://github.com/hut/ranger .

# default colorscheme.
# Copyright (C) 2009-2013  Roman Zimbelmann <hut@lepus.uberspace.de>
# This software is distributed under the terms of the GNU GPL version 3.

# ESTE ARCHIVO ES PERTENECIENTE AL IVAYLO KUZEV, YO SOLO LO MODIFIQUE Y ANADI
# COMENTARIOS PARA HACERLO MAS ENTENDIBLE PARA MI Y PARA QUIEN LO QUIERA VER
# TODOS LOS CREDITOS PARA EL, QUIEN ORIGINALMENTE CREO ESTE ARCHIVO (O ALMENOS LO TRAJO A LA LUZ)

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import default_colors, reverse, bold, normal, default


'''     TODO ESTO SE ENCUENTRA AL ENTRAR A RANGER, CARPETAS, ARCHIVOS, ETC
        EL RESTO DE CONFIG 'AVANZADA' SE ENCUENTRA MAS ABAJO

'''

# pylint: disable=too-many-branches,too-many-statements
class kiwi(ColorScheme):
    progress_bar_color = 232; #COLOR DE LA BARRA DE PROGRESO (RECOMIENDO NEGRO 232)

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        #-----------COLORES NORMALES BASICOS----------
        elif context.in_browser:
            if context.selected:
                attr = reverse
            else:
                attr = normal
            if context.empty or context.error:
                fg = 210;   #FOLDER VACIO (letras rojas "empty")
            if context.border:
                fg = 248;   #SEPARADOR (bordes blancos entre carpetas)
            if context.image:
                fg = 217;   #IMAGENES (png,jpeg,jpg,raw,etc)
            if context.video:
                fg = 153;   #VIDEOS (mp4,mov,mkv,etc)
            if context.audio:
                fg = 109;   #AUDIOS (mp3,ogg,etc)
            if context.document:
                fg = 189;   #ARCHIVOS (txt,docx,tar,config,etc)
            if context.container:
                fg = 146;   #COMPRIMIDOS (zip,rar,tgzip,etc)
            if context.directory:
                fg = 225;   #CARPETAS (folders)
                attr |= bold
            elif context.executable and not \
                    any((context.media, context.container,
                         context.fifo, context.socket)):
                fg = 230;   #EJECUTABLES (exe,bat,sh,msdos,etc) 

            #NO SE PARA QUE SIRVE ESTO DE SOCKET, NO CREO QUE SEA NECESARIO MODIFICARLO
            #NUNCA ENCONTRÉ EN QUE SITUACION SE ACTIVAN ESOS COLORES
            if context.socket:
                fg = 180
                attr |= bold
            if context.fifo or context.device:
                fg = 144
                if context.device:
                    attr |= bold

            if context.link:
                fg = 194 if context.good else 183; #CARPETAS/ARCHIVOS ENLAZADOS

            #ESTO ES PARA MARCAR CON T CUALQUIER ARCHIVO, AMBAS CONDICIONES EN <IF-ELSE>
            #DEBERIAN MARCARSE CON EL MISMO COLOR, YO LO HAGO POR SEGURIDAD
            if context.tag_marker and not context.selected:
                attr |= normal
                if fg in (174, 95):
                    fg = 193; #MARCAR CON T
                else:
                    fg = 193; #MARCAR CON T


        #-------------CONTEXTO SEELECCIONADO-----------
            if not context.selected and (context.cut or context.copied):
                fg = 194;   #COLOR AL CORTAR/COPIAR CARPETAS-ARCHIVOS
                #bg = 234;   #COLOR DE BACKGROUND OPCIONAL (RECOMIENDO NO USARLO)

            if context.main_column:
                if context.selected:
                    attr |= normal
                if context.marked:
                    attr |= normal
                    fg = 230; #SELECCIONAR CARPETAS (CON TECLA ESPACIO)
            if context.badinfo:
                if attr & reverse:
                    bg = 95; #CREO QUE ESTE NO HACE NADA
                else:
                    fg = 95; #CREO QUE ESTE NO HACE NADA


        #-------------TITLEBAR---------
        elif context.in_titlebar:
            #attr |= bold; #ATRIBUTO BOLD PARA LA BARRA <USUARIO+HOST>
            if context.hostname:
                attr |= bold
                fg = 147 if context.bad else 147 #COLOR DEL USUARIO+HOST
            elif context.directory:
                fg = 189; #COLOR DE LA RUTA DEL DIRECTORIO ACTUAL (EN LA TITLEBAR)
            elif context.tab:
                if context.good:
                    bg = 108; #COLOR DE LAS TABS (AL PRESIONAR CTRL+N)
            #folders linkeados
            elif context.link:
                fg = 183; #COLOR DE FOLDERS LINKEADOS EN EL DIR ACTUAL (TITLEBAR)


        #------------BARRA DE ESTATUS-----
        elif context.in_statusbar:
            if context.permissions:
                if context.good:
                    fg = 147; #PERMISOS EN LA TITLEBAR
                elif context.bad:
                    fg = 147; #PERMISOS EN LA TITLEBAR (POR SI ACASO)
            if context.marked:
                attr |= bold | reverse
                fg = 223; #LETRAS <MRK> AL MARCAR UN ARCHIVO CON ESPACIO
            if context.message:
                if context.bad:
                    attr |= bold
                    fg = 174
            if context.loaded:
                bg = self.progress_bar_color
            if context.vcsinfo:
                fg = 116
                attr &= ~bold
            if context.vcscommit:
                fg = 144
                attr &= ~bold


        #------------INFORMACION NO UTIL(CREO)-----------
        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = 116

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    fg = self.progress_bar_color
                else:
                    bg = self.progress_bar_color

        if context.vcsfile and not context.selected:
            attr &= ~bold
            if context.vcsconflict:
                fg = 95
            elif context.vcschanged:
                fg = 174
            elif context.vcsunknown:
                fg = 174
            elif context.vcsstaged:
                fg = 108
            elif context.vcssync:
                fg = 108
            elif context.vcsignored:
                fg = default

        elif context.vcsremote and not context.selected:
            attr &= ~bold
            if context.vcssync:
                fg = 108
            elif context.vcsbehind:
                fg = 174
            elif context.vcsahead:
                fg = 116
            elif context.vcsdiverged:
                fg = 95
            elif context.vcsunknown:
                fg = 174

        return fg, bg, attr

# Language adapter configuration.
#
# To add another translation, copy the Chinese entry, change its key to the
# Ren'Py language/directory name (for example, "Spanish"), and replace only the
# values in that entry. Normal dialogue and string translations remain in
# tl/<Language>; this table handles the runtime-only text and resources that
# Ren'Py cannot discover by itself.
init -1000 python:
    _localization_profiles = {
        "Chinese": {
            "display_name": "Chinese",
            "autodetect": True,
            "legacy_ids": ("chinese",),
            "locale_languages": ("zh",),
            "locale_regions": ("cn", "tw", "hk", "zh"),
            "image_directory": "tl/Chinese/images",
            "image_button": "Chinese Images",
            "extra_image_overrides": {},
            # Size of the handwritten transcription shown on the Gilgamesh paper. The original screen uses 16
            "gil_text_size": 24,
            "preserve_cuneiform_english": True,
            "input_aliases": {
                "剪刀": "Scissors", "剪子": "Scissors", "剪": "Scissors",
                "大剪刀": "Scissors", "裁缝剪": "Shears", "裁缝剪刀": "Shears",
                "理发剪": "Clippers", "理发剪刀": "Clippers", "剪切器": "Cutters",
                "梦魇": "Nightmare", "噩梦": "Nightmare", "恶梦": "Nightmare",
                "坏梦": "Bad Dream", "可怕的梦": "Bad Dream", "梦": "Dream",
                "夜惊": "night terror", "夜惊症": "night terror",
                "胡姆巴巴": "Humbaba", "洪巴巴": "Humbaba", "胡巴巴": "Hubaba", "虎目巴巴": "Humbaba", "虎木巴巴": "Humbaba",
                "胡玛玛": "Humama", "胡瓦瓦": "Huwawa",
            },
            "secret_name_aliases": {
                "吉尔伽美什": "Gilgamesh", "吉加美士": "Gilgamesh",
                "鸠格米西": "Gilgameš", "基加美修": "Bilgames",
                "帕比尔伽美什": "Pabilgames", "恩奇都": "Enkidu",
                "恩基都": "Enkidu", "恩启都": "Enkidu",
                "胡姆巴巴": "Humbaba", "洪巴巴": "Humbaba", "虎目巴巴": "Humbaba", "虎木巴巴": "Humbaba",
                "胡巴巴": "Hubaba", "胡玛玛": "Humama", "胡瓦瓦": "Huwawa",
            },
            "pronouns": {
                "male": ("他", "他", "他", "他", "他", "他", "他", "他"),
                "female": ("她", "她", "她", "她", "她", "她", "她", "她"),
                "neutral": ("TA", "TA", "TA", "TA", "TA", "TA", "TA", "TA"),
            },
            "intro_menu_sources": (
                "You woke every morning to silence.",
                "You woke every morning to the chorus of birds, and fell asleep every evening to the roaring of crickets.",
            ),
            "birthday_note_source": "{size=16}{font=fonts/segoesc.ttf}{color=#45413c}{alpha=*0.6}I saw this intriguing article while I was researching online and it seemed like the kind of thing that you would enjoy. It is wonderful what you can find on the internet these days. It was tough to find the book but we were able to track down this volume second-hand, which the bookshop owner told us may be one of the only remaining copies! I hope that you will enjoy it. \n\nPlease give our best to your mum and dad and tell them that we are doing well here. The weather has been lovely.\n\nHappy birthday, [povname].\n\nLove Grandma and Grandpa.{/color}{/font}{/size}",
            "finale_titles": {
                "Cobbler": "鞋匠", "Trickster": "骗子", "Crow": "乌鸦",
                "Specter": "幽灵", "Winter Rose": "冬玫瑰", "Fool": "傻子",
                "Water Nixie": "水精灵", "Giant": "巨人", "Bushranger": "绿林好汉",
                "Butcher": "屠夫", "Aristocrat": "贵族",
                "Warrior-Poet": "武士诗人", "Heirophant": "教皇",
            },
        },

        # Example adapter. Uncomment after tl/Spanish and its optional images
        # are ready, then fill the dictionaries above with Spanish values.
        # "Spanish": {
        #     "display_name": "Spanish",
        #     # Change to True only after the Spanish translation is complete.
        #     "autodetect": False,
        #     "legacy_ids": (),
        #     "locale_languages": ("es",),
        #     "locale_regions": ("es", "mx", "ar", "bo", "cl", "co", "cr",
        #         "cu", "do", "ec", "gt", "hn", "ni", "pa", "pe", "pr",
        #         "py", "sv", "uy", "ve"),
        #     "image_directory": "tl/Spanish/images",
        #     "image_button": "Spanish Images",
        #     "gil_text_size": 20,
        #     # Optional: {"original/path.png": "tl/Spanish/images/custom.png"}
        #     "extra_image_overrides": {},
        #     "preserve_cuneiform_english": True,
        #     "input_aliases": {},
        #     "secret_name_aliases": {},
        #     "pronouns": {},
        #     "intro_menu_sources": (),
        #     "birthday_note_source": None,
        #     "finale_titles": {},
        # },
    }

    def _active_localization_profile():
        language = renpy.game.preferences.language
        return language, _localization_profiles.get(language)

    def _localized_gil_text_size():
        _language, profile = _active_localization_profile()
        return profile.get("gil_text_size", 16) if profile else 16


# Generated resource overrides for localized images.
# Keep translated images under the profile's image_directory.

init -999 python:
    import os

    def _backup_loose_fonts_for_archive():
        font_directory = os.path.join(renpy.config.gamedir, "fonts")
        if not os.path.isdir(font_directory):
            return

        archived_files = set()
        for _archive_name, archive_index in renpy.loader.archives:
            archived_files.update(archive_index)

        for filename in os.listdir(font_directory):
            if not filename.lower().endswith((".ttf", ".otf")):
                continue
            if "fonts/" + filename not in archived_files:
                continue

            source = os.path.join(font_directory, filename)
            backup = source + ".bak"
            if os.path.exists(backup):
                continue

            try:
                os.replace(source, backup)
            except OSError as error:
                renpy.log("Chinese font override could not back up {}: {}".format(source, error))

        renpy.loader.loadable_cache.clear()

    _backup_loose_fonts_for_archive()

init 999 python:
    _chinese_image_overrides = {
        "images/bg credits.png": "tl/Chinese/images/bg credits.png",
        "images/contents_ground.png": "tl/Chinese/images/contents_ground.png",
        "images/contents_hover.png": "tl/Chinese/images/contents_hover.png",
        "images/contents_idle.png": "tl/Chinese/images/contents_idle.png",
        "images/contents_note.png": "tl/Chinese/images/contents_note.png",
        "images/creepiestClosed.png": "tl/Chinese/images/creepiestClosed.png",
        "images/creepiestClosedHover.png": "tl/Chinese/images/creepiestClosedHover.png",
        "images/creepiestOpen.png": "tl/Chinese/images/creepiestOpen.png",
        "images/essay1.png": "tl/Chinese/images/essay1.png",
        "images/essay2.png": "tl/Chinese/images/essay2.png",
        "images/essay3.png": "tl/Chinese/images/essay3.png",
        "images/essay4.png": "tl/Chinese/images/essay4.png",
        "images/essay5.png": "tl/Chinese/images/essay5.png",
        "images/essay6.png": "tl/Chinese/images/essay6.png",
        "images/GilgameshNote.png": "tl/Chinese/images/GilgameshNote.png",
        "images/GilgameshOpen-name.png": "tl/Chinese/images/GilgameshOpen-name.png",
        "images/GilgameshOpen.png": "tl/Chinese/images/GilgameshOpen.png",
        "images/gilgameshPathOpen.png": "tl/Chinese/images/gilgameshPathOpen.png",
        "images/gilgameshPathOpenHover.png": "tl/Chinese/images/gilgameshPathOpenHover.png",
        "images/diaryOpen.png": "tl/Chinese/images/diaryOpen.png",
        "gui/about.png": "tl/Chinese/images/gui/about.png",
        "gui/bookmark-s.png": "tl/Chinese/images/gui/bookmark-s.png",
        "gui/bookmark.png": "tl/Chinese/images/gui/bookmark.png",
        "gui/game_menu(backup).png": "tl/Chinese/images/gui/game_menu(backup).png",
        "gui/main_menu.png": "tl/Chinese/images/gui/main_menu.png",
        "gui/main_menu2.png": "tl/Chinese/images/gui/main_menu2.png",
        "images/map1-old.png": "tl/Chinese/images/map1-old.png",
        "images/map1.png": "tl/Chinese/images/map1.png",
        "images/mapBlank-house.png": "tl/Chinese/images/mapBlank-house.png",
        "images/mapBlank-village.png": "tl/Chinese/images/mapBlank-village.png",
        "images/Marginalia/noteCareful.png": "tl/Chinese/images/Marginalia/noteCareful.png",
        "images/Marginalia/noteChance.png": "tl/Chinese/images/Marginalia/noteChance.png",
        "images/Marginalia/noteCrumbs.png": "tl/Chinese/images/Marginalia/noteCrumbs.png",
        "images/Marginalia/noteDeal.png": "tl/Chinese/images/Marginalia/noteDeal.png",
        "images/Marginalia/noteDoor.png": "tl/Chinese/images/Marginalia/noteDoor.png",
        "images/Marginalia/noteEaten.png": "tl/Chinese/images/Marginalia/noteEaten.png",
        "images/Marginalia/noteFood.png": "tl/Chinese/images/Marginalia/noteFood.png",
        "images/Marginalia/noteFree.png": "tl/Chinese/images/Marginalia/noteFree.png",
        "images/Marginalia/noteHome.png": "tl/Chinese/images/Marginalia/noteHome.png",
        "images/Marginalia/noteListen.png": "tl/Chinese/images/Marginalia/noteListen.png",
        "images/Marginalia/noteListen2.png": "tl/Chinese/images/Marginalia/noteListen2.png",
        "images/Marginalia/noteName.png": "tl/Chinese/images/Marginalia/noteName.png",
        "images/Marginalia/noteReturn.png": "tl/Chinese/images/Marginalia/noteReturn.png",
        "images/Marginalia/noteSay.png": "tl/Chinese/images/Marginalia/noteSay.png",
        "images/Marginalia/noteSilence.png": "tl/Chinese/images/Marginalia/noteSilence.png",
        "images/Marginalia/noteStop.png": "tl/Chinese/images/Marginalia/noteStop.png",
        "images/Marginalia/noteWaiting.png": "tl/Chinese/images/Marginalia/noteWaiting.png",
        "images/Marginalia/noteWolf.png": "tl/Chinese/images/Marginalia/noteWolf.png",
        "images/Names/bat.png": "tl/Chinese/images/Names/bat.png",
        "images/Names/bc.png": "tl/Chinese/images/Names/bc.png",
        "images/Names/boys.png": "tl/Chinese/images/Names/boys.png",
        "images/Names/cockatoo.png": "tl/Chinese/images/Names/cockatoo.png",
        "images/Names/crowshrike.png": "tl/Chinese/images/Names/crowshrike.png",
        "images/Names/dg.png": "tl/Chinese/images/Names/dg.png",
        "images/Names/echidna.png": "tl/Chinese/images/Names/echidna.png",
        "images/Names/echidna2.png": "tl/Chinese/images/Names/echidna2.png",
        "images/Names/eg.png": "tl/Chinese/images/Names/eg.png",
        "images/Names/gilgamesh.png": "tl/Chinese/images/Names/gilgamesh.png",
        "images/Names/gm.png": "tl/Chinese/images/Names/gm.png",
        "images/Names/go.png": "tl/Chinese/images/Names/go.png",
        "images/Names/goblin1.png": "tl/Chinese/images/Names/goblin1.png",
        "images/Names/goblin2.png": "tl/Chinese/images/Names/goblin2.png",
        "images/Names/goblin3.png": "tl/Chinese/images/Names/goblin3.png",
        "images/Names/goblin4.png": "tl/Chinese/images/Names/goblin4.png",
        "images/Names/goblinqueen-s.png": "tl/Chinese/images/Names/goblinqueen-s.png",
        "images/Names/goblinqueen.png": "tl/Chinese/images/Names/goblinqueen.png",
        "images/Names/gutterking.png": "tl/Chinese/images/Names/gutterking.png",
        "images/Names/gutterlings.png": "tl/Chinese/images/Names/gutterlings.png",
        "images/Names/h.png": "tl/Chinese/images/Names/h.png",
        "images/Names/humbaba.png": "tl/Chinese/images/Names/humbaba.png",
        "images/Names/may.png": "tl/Chinese/images/Names/may.png",
        "images/Names/mir.png": "tl/Chinese/images/Names/mir.png",
        "images/Names/miw.png": "tl/Chinese/images/Names/miw.png",
        "images/Names/mum.png": "tl/Chinese/images/Names/mum.png",
        "images/Names/mushroom-s.png": "tl/Chinese/images/Names/mushroom-s.png",
        "images/Names/mushroom.png": "tl/Chinese/images/Names/mushroom.png",
        "images/Names/mushroom2-s.png": "tl/Chinese/images/Names/mushroom2-s.png",
        "images/Names/mushroom2.png": "tl/Chinese/images/Names/mushroom2.png",
        "images/Names/mushroom3-s.png": "tl/Chinese/images/Names/mushroom3-s.png",
        "images/Names/mushroom3.png": "tl/Chinese/images/Names/mushroom3.png",
        "images/Names/mushroom4-s.png": "tl/Chinese/images/Names/mushroom4-s.png",
        "images/Names/mushroom4.png": "tl/Chinese/images/Names/mushroom4.png",
        "images/Names/mys.png": "tl/Chinese/images/Names/mys.png",
        "images/Names/mysFrog.png": "tl/Chinese/images/Names/mysFrog.png",
        "images/Names/p1.png": "tl/Chinese/images/Names/p1.png",
        "images/Names/p2.png": "tl/Chinese/images/Names/p2.png",
        "images/Names/p3.png": "tl/Chinese/images/Names/p3.png",
        "images/Names/rat.png": "tl/Chinese/images/Names/rat.png",
        "images/Names/sc.png": "tl/Chinese/images/Names/sc.png",
        "images/Names/sh.png": "tl/Chinese/images/Names/sh.png",
        "images/Names/sm-s.png": "tl/Chinese/images/Names/sm-s.png",
        "images/Names/sm.png": "tl/Chinese/images/Names/sm.png",
        "images/Names/som.png": "tl/Chinese/images/Names/som.png",
        "images/Names/thief.png": "tl/Chinese/images/Names/thief.png",
        "images/Names/thiefmum.png": "tl/Chinese/images/Names/thiefmum.png",
        "images/Names/toad-gecko.png": "tl/Chinese/images/Names/toad-gecko.png",
        "images/Names/toad-quoll.png": "tl/Chinese/images/Names/toad-quoll.png",
        "images/Names/toad-rat.png": "tl/Chinese/images/Names/toad-rat.png",
        "images/Names/toad.png": "tl/Chinese/images/Names/toad.png",
        "images/Names/town.png": "tl/Chinese/images/Names/town.png",
        "images/Names/well.png": "tl/Chinese/images/Names/well.png",
        "images/Names/wib.png": "tl/Chinese/images/Names/wib.png",
        "images/Names/witch-old.png": "tl/Chinese/images/Names/witch-old.png",
        "images/Names/witch.png": "tl/Chinese/images/Names/witch.png",
        "images/Names/wives.png": "tl/Chinese/images/Names/wives.png",
        "images/Names/you.png": "tl/Chinese/images/Names/you.png",
        "images/newsArticle.png": "tl/Chinese/images/newsArticle.png",
        "images/note1Open.png": "tl/Chinese/images/note1Open.png",
        "images/photo-5.png": "tl/Chinese/images/photo-5.png",
        "images/photo-6.png": "tl/Chinese/images/photo-6.png",
        "images/posterOpen.png": "tl/Chinese/images/posterOpen.png",
        "images/Backgrounds/contents-alex.png": "tl/Chinese/images/Backgrounds/contents-alex.png",
        "images/Backgrounds/contents-georgia.png": "tl/Chinese/images/Backgrounds/contents-georgia.png",
    }

    _chinese_image_overrides = dict(
        (original.casefold(), localized)
        for original, localized in _chinese_image_overrides.items()
    )

    _original_loader_load = renpy.loader.load

    def _localized_image_enabled(language):
        states = getattr(persistent, "localization_image_overrides", None) or {}
        if language in states:
            return states[language]
        if language == "Chinese":
            return persistent.chinese_image_override_enabled
        return True

    def _toggle_localized_image_override(language):
        states = dict(getattr(persistent, "localization_image_overrides", None) or {})
        states[language] = not _localized_image_enabled(language)
        persistent.localization_image_overrides = states
        if language == "Chinese":
            persistent.chinese_image_override_enabled = states[language]
        renpy.save_persistent()
        renpy.free_memory()
        renpy.restart_interaction()

    def _chinese_image_load(name, directory=None, tl=True):
        language, profile = _active_localization_profile()
        if tl and profile and profile.get("image_directory") and _localized_image_enabled(language):
            normalized_name = name.replace("\\", "/").lstrip("/").casefold()
            extra = dict(
                (source.casefold(), target)
                for source, target in profile.get("extra_image_overrides", {}).items()
            )
            localized = extra.get(normalized_name)
            template = _chinese_image_overrides.get(normalized_name) if localized is None else None

            if localized is None and template is None and directory:
                normalized_directory = directory.replace("\\", "/").strip("/").casefold()
                combined_name = normalized_directory + "/" + normalized_name
                localized = extra.get(combined_name)
                template = _chinese_image_overrides.get(combined_name) if localized is None else None

            if template is not None:
                prefix = "tl/Chinese/images"
                localized = profile["image_directory"].rstrip("/") + template[len(prefix):]

            if localized is not None and renpy.loadable(localized):
                return _original_loader_load(localized, directory=None, tl=False)

        return _original_loader_load(name, directory=directory, tl=tl)

    renpy.loader.load = _chinese_image_load


# Chinese answer aliases for the original input checks.
# Unrecognized input is returned unchanged so the original flow remains intact.

init 999 python:
    import unicodedata

    def _chinese_input_key(value):
        if isinstance(value, str):
            return unicodedata.normalize("NFKC", value).strip()
        return value

    _original_chinese_input = renpy.input

    def _chinese_input(prompt, *args, **kwargs):
        prompt = renpy.translate_string(prompt)
        answer = _original_chinese_input(prompt, *args, **kwargs)
        _language, profile = _active_localization_profile()
        aliases = profile.get("input_aliases", {}) if profile else {}
        return aliases.get(_chinese_input_key(answer), answer)

    _original_chinese_name_func = name_func

    def _chinese_name_func(newstring):
        _language, profile = _active_localization_profile()
        aliases = profile.get("secret_name_aliases", {}) if profile else {}
        normalized_name = aliases.get(_chinese_input_key(newstring), newstring)
        _original_chinese_name_func(normalized_name)

    renpy.input = _chinese_input
    name_func = _chinese_name_func


translate Chinese strings:

    old "{i}Answer thee my riddles three:{/i}"
    new "{i}回答我的三个谜语：{/i}"

    old "{i}I name you and bind you:{/i}"
    new "{i}我呼唤汝名，将你束缚：{/i}"


# Localize interpolated player pronouns after Ren'Py has translated the line.

init python:
    def _player_pronoun_set():
        value = getattr(persistent, "he", "he")

        if value in ("she", "She", "她"):
            return "female"
        elif value in ("they", "They", "TA", "ta", "他们", "她们"):
            return "neutral"
        else:
            return "male"

    def _sync_localized_player_terms():
        global he, He, his, His, him, Him, Hes, hes, povname, introMenuSentence

        pronoun_set = _player_pronoun_set()
        language, profile = _active_localization_profile()

        localized_pronouns = profile.get("pronouns", {}) if profile else {}
        if pronoun_set in localized_pronouns:
            he, He, his, His, him, Him, Hes, hes = localized_pronouns[pronoun_set]
        else:
            english = {
                "male": ("he", "He", "his", "His", "him", "Him", "He's", "he's"),
                "female": ("she", "She", "her", "Her", "her", "Her", "She's", "she's"),
                "neutral": ("they", "They", "their", "Their", "them", "Them", "They are", "they are"),
            }[pronoun_set]

            he, He, his, His, him, Him, Hes, hes = english

        # Player-entered names are data, not translation keys.
        povname = getattr(persistent, "povname", "")

        # These strings are assigned through _() and interpolated later, so
        # Ren'Py does not translate them a second time by itself.
        dynamic_sources = []
        for candidate_profile in _localization_profiles.values():
            dynamic_sources.extend(candidate_profile.get("intro_menu_sources", ()))
        current_dynamic = globals().get("introMenuSentence", None)
        for source in dynamic_sources:
            known_values = [source]
            for candidate_language in _localization_profiles:
                known_values.append(renpy.translate_string(source, candidate_language))
            if current_dynamic in known_values:
                introMenuSentence = renpy.translate_string(source, language) if profile else source
                break

    def _chinese_patch_label_callback(label, abnormal):
        if label != "gilgameshStory":
            return

        renpy.store.gilWho = False
        renpy.store.gilWalls = False
        renpy.store.gilStone = False
        renpy.store.gilEnkidu = False
        renpy.store.gilNext = False
        renpy.store.gilDeath = False
        renpy.store.gilHumbaba = False
        renpy.store.gilDo = False
        renpy.store.gilCome = False

    config.change_language_callbacks.append(_sync_localized_player_terms)
    config.after_load_callbacks.append(_sync_localized_player_terms)
    config.start_callbacks.append(_sync_localized_player_terms)
    # The original script copies the persistent English values one by one.
    # Refresh after each Python statement so the patch does not need to replace it.
    config.python_callbacks.append(_sync_localized_player_terms)
    config.label_callbacks.append(_chinese_patch_label_callback)


# Keep Gilgamesh's encoded dialogue in English where configured, so
# EasyCuneiform can render it.
# The paper transcription in gilText is translated separately.

init 999 python:
    class _ChineseCuneiformCharacter(renpy.character.ADVCharacter):
        def prefix_suffix(self, thing, prefix, body, suffix):
            _language, profile = _active_localization_profile()
            preserve_english = profile and profile.get("preserve_cuneiform_english")
            if thing != "what" or not preserve_english:
                return renpy.character.ADVCharacter.prefix_suffix(
                    self, thing, prefix, body, suffix
                )

            def sub(value):
                return renpy.substitutions.substitute(
                    value, force=False, translate=False
                )[0]

            thingvar_quoted = "[[" + thing + "]"
            thingvar = "[" + thing + "]"

            if not renpy.config.new_substitutions:
                return prefix + body + suffix
            elif renpy.config.who_what_sub_compat == 0:
                pattern = sub(prefix + thingvar_quoted + suffix)
                return pattern.replace(thingvar, sub(body))
            elif renpy.config.who_what_sub_compat == 1:
                pattern = sub(sub(prefix) + thingvar_quoted + sub(suffix))
                return pattern.replace(thingvar, sub(body))
            else:
                return sub(prefix) + sub(body) + sub(suffix)

    gil = _ChineseCuneiformCharacter(kind=gil)
    gBlank = _ChineseCuneiformCharacter(kind=gBlank)


init python:
    def _localized_runtime_translation(value):
        language, profile = _active_localization_profile()
        if profile and isinstance(value, str):
            return renpy.translate_string(value, language)

        return value

    def _sync_localized_birthday_note():
        _language, profile = _active_localization_profile()
        source = profile.get("birthday_note_source") if profile else None
        if source is None:
            for candidate_profile in _localization_profiles.values():
                source = candidate_profile.get("birthday_note_source")
                if source is not None:
                    break
        if source is not None:
            renpy.store.birthdayNote = _localized_runtime_translation(source)

    _chinese_original_show = renpy.config.show

    def _chinese_runtime_show(name, *args, **kwargs):
        if isinstance(name, tuple) and len(name) > 1 and name[0] in ("text", "vtext"):
            try:
                source = renpy.python.py_eval(name[1])
                translated = _localized_runtime_translation(source)

                if translated != source:
                    name = name[:1] + (repr(translated),) + name[2:]
            except Exception:
                pass

        return _chinese_original_show(name, *args, **kwargs)

    renpy.config.show = _chinese_runtime_show

    _chinese_original_ui_text = renpy.ui.text

    def _chinese_runtime_ui_text(value, *args, **kwargs):
        return _chinese_original_ui_text(_localized_runtime_translation(value), *args, **kwargs)

    renpy.ui.text = _chinese_runtime_ui_text

    _chinese_original_say_menu_text_filter = renpy.config.say_menu_text_filter

    def _chinese_say_menu_text_filter(value):
        if _chinese_original_say_menu_text_filter is not None:
            value = _chinese_original_say_menu_text_filter(value)

        _language, profile = _active_localization_profile()
        if not profile or not isinstance(value, str):
            return value

        marker = "[persistent.finaleTitle]"
        if marker not in value:
            return value

        english_title = getattr(renpy.store.persistent, "finaleTitle", None)
        localized_title = profile.get("finale_titles", {}).get(english_title)
        if localized_title is None and english_title is not None:
            candidate = renpy.translate_string(english_title, _language)
            if candidate != english_title:
                localized_title = candidate
        if localized_title is not None:
            value = value.replace(marker, localized_title)

        return value

    renpy.config.say_menu_text_filter = _chinese_say_menu_text_filter

    renpy.config.change_language_callbacks.append(_sync_localized_birthday_note)
    renpy.config.after_load_callbacks.append(_sync_localized_birthday_note)
    renpy.config.start_callbacks.append(_sync_localized_birthday_note)


default persistent.chinese_image_override_enabled = True
default persistent.localization_image_overrides = {}

# Let Ren'Py choose the first-run language from the user's system locale.
define config.enable_language_autodetect = True


init 999 python:
    def _chinese_locale_to_language(locale, region):
        for language, profile in _localization_profiles.items():
            if not profile.get("autodetect", False):
                continue
            if locale not in profile.get("locale_languages", ()):
                continue
            regions = profile.get("locale_regions", ())
            if not regions or region in regions:
                return language
        return None

    config.locale_to_language_function = _chinese_locale_to_language

    def _refresh_chinese_window_title():
        interface = getattr(renpy.game, "interface", None)
        if interface is not None:
            interface.set_window_caption(force=True)

    def _migrate_lowercase_chinese_language():
        # Migrate legacy directory names without overriding a fresh choice.
        current = renpy.game.preferences.language
        for language, profile in _localization_profiles.items():
            if current in profile.get("legacy_ids", ()):
                renpy.change_language(language)
                renpy.save_persistent()
                break

    _refresh_chinese_window_title()

    config.start_callbacks.append(_migrate_lowercase_chinese_language)
    config.change_language_callbacks.append(_refresh_chinese_window_title)


init python early hide:
    _chinese_original_show_screen = renpy.show_screen

    def _chinese_show_screen(screen_name, *args, **kwargs):
        if screen_name == "preferences":
            screen_name = "chinese_preferences"
        elif screen_name == "gilgameshText":
            screen_name = "localized_gilgameshText"
        return _chinese_original_show_screen(screen_name, *args, **kwargs)

    renpy.show_screen = _chinese_show_screen


# This mirrors the game's current preferences screen, with the Chinese entries
# placed in the author's existing Language column. The original screens.rpy is
# left untouched.
screen chinese_preferences():

    tag menu

    add "/images/bg page.png"

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox xpos 30 ypos 160:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    label _("Language")
                    textbutton "English" action Language(None)
                    for language, profile in _localization_profiles.items():
                        textbutton _(profile["display_name"]) action Language(language)
                        if renpy.game.preferences.language == language and profile.get("image_directory"):
                            textbutton _(profile["image_button"]):
                                action Function(_toggle_localized_image_override, language)
                                selected _localized_image_enabled(language)

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Ambience Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

                vbox:
                    style_prefix "radio"
                    label _("Safe For Work Mode")
                    textbutton _("Off") action SetVariable("persistent.sfw", False)
                    textbutton _("On") action SetVariable("persistent.sfw", True)

                vbox:
                    textbutton _("Change Name & Pronouns") action Play("sound", "audio/page-flip.mp3"), ShowMenu("contents")


# Replacement for the original gilgameshText screen. The original screen has
# a hard-coded ``size 16``; this copy keeps its tag and layout while reading
# the configurable size from the active language profile.
screen localized_gilgameshText():

    tag gilgameshText
    zorder 101

    frame:
        has hbox:
            spacing 5
            box_wrap True
            xpos 280
            ypos 750
            xalign 0.5
            yalign 0.5
            xsize 530
            ysize 300
            transform:
                rotate 2.0
                text gilText size _localized_gil_text_size() font "fonts/segoesc.ttf" color "#45413c" textalign 0.1
                alpha 0.9

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on junio 29, 2023, at 18:13
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'prueba de sumacion'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\saezr\\OneDrive\\Escritorio\\prueba de sumacion\\prueba de sumacion.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0,1.0,1.0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICION" ---
text = visual.TextStim(win=win, name='text',
    text='¿Cuán probable es que se presente la imagen y el sonido desagradable?',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
excitadordetransferencia = visual.ImageStim(
    win=win,
    name='excitadordetransferencia', 
    image=EXCITADOR_DE_TRANSFERENCIA_ADQUISICION, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
ESCALA_EXPECTATIVA_excitadordetransferencia_PDS = visual.Slider(win=win, name='ESCALA_EXPECTATIVA_excitadordetransferencia_PDS',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Poco probable" , "Muy probable"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-2, readOnly=False)
EIPERRO_excitadordetransferencia = visual.ImageStim(
    win=win,
    name='EIPERRO_excitadordetransferencia', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
EISONIDO_excitadordetransferencia = sound.Sound(EI_SONIDO, secs=0.7, stereo=True, hamming=True,
    name='EISONIDO_excitadordetransferencia')
EISONIDO_excitadordetransferencia.setVolume(1.0)

# --- Initialize components for Routine "ITI_excitadordetransferencia_PDS" ---
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "ESTIMULO_COMPUESTO_INHIBIDOR" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='¿Cuán probable es que se presente la imagen y el sonido desagradable?',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
jeje = visual.ImageStim(
    win=win,
    name='jeje', 
    image=INHIBIDOR_A_PRUEBA_ADQUISICION, mask=None, anchor='center',
    ori=0.0, pos=(1.0, 0.0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
jiji = visual.ImageStim(
    win=win,
    name='jiji', 
    image=EXCITADOR_DE_TRANSFERENCIA_ADQUISICION, mask=None, anchor='center',
    ori=0.0, pos=(0.0, 1.0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Poco probable" , "Muy probable"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-3, readOnly=False)

# --- Initialize components for Routine "ITI_estimulocompuestoinhibidor_PDS" ---
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "ESTIMULO_COMPUESTO_NEUTRO" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='¿Cuán probable es que se presente la imagen y el sonido desagradable?',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
jojo = visual.ImageStim(
    win=win,
    name='jojo', 
    image=ESTIMULO_NEUTRO_ADQUISICION, mask=None, anchor='center',
    ori=0.0, pos=(1.0, 0.0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
juju = visual.ImageStim(
    win=win,
    name='juju', 
    image=EXCITADOR_DE_TRANSFERENCIA_ADQUISICION, mask=None, anchor='center',
    ori=0.0, pos=(0, 1.0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
slider_2 = visual.Slider(win=win, name='slider_2',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Poco probable" , "Muy probable"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-3, readOnly=False)

# --- Initialize components for Routine "ITI_estimulocompuestoneutro_PDS" ---
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "ESTIMULO_EXCITATORIO_PDS" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='¿Cuán probable es que se presente la imagen y el sonido desagradable?',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
joasjoas = visual.ImageStim(
    win=win,
    name='joasjoas', 
    image=ESTIMULO_EXCITATORIO_ADQUISICION, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
slider_3 = visual.Slider(win=win, name='slider_3',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Poco probable" , "Muy probable"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-2, readOnly=False)
ei = visual.ImageStim(
    win=win,
    name='ei', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
eisonido = sound.Sound(EI_SONIDO, secs=0.7, stereo=True, hamming=True,
    name='eisonido')
eisonido.setVolume(1.0)

# --- Initialize components for Routine "ITI_estimuloexcitatorio_PDS" ---
polygon_5 = visual.ShapeStim(
    win=win, name='polygon_5', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials_excitadordetransferencia = data.TrialHandler(nReps=14.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_excitadordetransferencia')
thisExp.addLoop(trials_excitadordetransferencia)  # add the loop to the experiment
thisTrials_excitadordetransferencia = trials_excitadordetransferencia.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_excitadordetransferencia.rgb)
if thisTrials_excitadordetransferencia != None:
    for paramName in thisTrials_excitadordetransferencia:
        exec('{} = thisTrials_excitadordetransferencia[paramName]'.format(paramName))

for thisTrials_excitadordetransferencia in trials_excitadordetransferencia:
    currentLoop = trials_excitadordetransferencia
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_excitadordetransferencia.rgb)
    if thisTrials_excitadordetransferencia != None:
        for paramName in thisTrials_excitadordetransferencia:
            exec('{} = thisTrials_excitadordetransferencia[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICION" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.reset()
    EIPERRO_excitadordetransferencia.setImage(EI_FOTO)
    EISONIDO_excitadordetransferencia.setSound(EI_SONIDO, secs=0.7, hamming=True)
    EISONIDO_excitadordetransferencia.setVolume(1.0, log=False)
    # keep track of which components have finished
    ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICIONComponents = [text, excitadordetransferencia, ESCALA_EXPECTATIVA_excitadordetransferencia_PDS, EIPERRO_excitadordetransferencia, EISONIDO_excitadordetransferencia]
    for thisComponent in ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICIONComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICION" ---
    while continueRoutine and routineTimer.getTime() < 4.8:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                text.setAutoDraw(False)
        
        # *excitadordetransferencia* updates
        if excitadordetransferencia.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            excitadordetransferencia.frameNStart = frameN  # exact frame index
            excitadordetransferencia.tStart = t  # local t and not account for scr refresh
            excitadordetransferencia.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(excitadordetransferencia, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'excitadordetransferencia.started')
            excitadordetransferencia.setAutoDraw(True)
        if excitadordetransferencia.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > excitadordetransferencia.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                excitadordetransferencia.tStop = t  # not accounting for scr refresh
                excitadordetransferencia.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'excitadordetransferencia.stopped')
                excitadordetransferencia.setAutoDraw(False)
        
        # *ESCALA_EXPECTATIVA_excitadordetransferencia_PDS* updates
        if ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.frameNStart = frameN  # exact frame index
            ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.tStart = t  # local t and not account for scr refresh
            ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ESCALA_EXPECTATIVA_excitadordetransferencia_PDS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.started')
            ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.setAutoDraw(True)
        if ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.tStop = t  # not accounting for scr refresh
                ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.stopped')
                ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.setAutoDraw(False)
        
        # *EIPERRO_excitadordetransferencia* updates
        if EIPERRO_excitadordetransferencia.status == NOT_STARTED and tThisFlip >= 4.1-frameTolerance:
            # keep track of start time/frame for later
            EIPERRO_excitadordetransferencia.frameNStart = frameN  # exact frame index
            EIPERRO_excitadordetransferencia.tStart = t  # local t and not account for scr refresh
            EIPERRO_excitadordetransferencia.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EIPERRO_excitadordetransferencia, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EIPERRO_excitadordetransferencia.started')
            EIPERRO_excitadordetransferencia.setAutoDraw(True)
        if EIPERRO_excitadordetransferencia.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EIPERRO_excitadordetransferencia.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                EIPERRO_excitadordetransferencia.tStop = t  # not accounting for scr refresh
                EIPERRO_excitadordetransferencia.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EIPERRO_excitadordetransferencia.stopped')
                EIPERRO_excitadordetransferencia.setAutoDraw(False)
        # start/stop EISONIDO_excitadordetransferencia
        if EISONIDO_excitadordetransferencia.status == NOT_STARTED and tThisFlip >= 4.1-frameTolerance:
            # keep track of start time/frame for later
            EISONIDO_excitadordetransferencia.frameNStart = frameN  # exact frame index
            EISONIDO_excitadordetransferencia.tStart = t  # local t and not account for scr refresh
            EISONIDO_excitadordetransferencia.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('EISONIDO_excitadordetransferencia.started', tThisFlipGlobal)
            EISONIDO_excitadordetransferencia.play(when=win)  # sync with win flip
        if EISONIDO_excitadordetransferencia.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EISONIDO_excitadordetransferencia.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                EISONIDO_excitadordetransferencia.tStop = t  # not accounting for scr refresh
                EISONIDO_excitadordetransferencia.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EISONIDO_excitadordetransferencia.stopped')
                EISONIDO_excitadordetransferencia.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICIONComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICION" ---
    for thisComponent in ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICIONComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_excitadordetransferencia.addData('ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.response', ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.getRating())
    trials_excitadordetransferencia.addData('ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.rt', ESCALA_EXPECTATIVA_excitadordetransferencia_PDS.getRT())
    EISONIDO_excitadordetransferencia.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.800000)
    
    # --- Prepare to start Routine "ITI_excitadordetransferencia_PDS" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ITI_excitadordetransferencia_PDSComponents = [polygon_4]
    for thisComponent in ITI_excitadordetransferencia_PDSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI_excitadordetransferencia_PDS" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_4.started')
            polygon_4.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_excitadordetransferencia_PDSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI_excitadordetransferencia_PDS" ---
    for thisComponent in ITI_excitadordetransferencia_PDSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI_excitadordetransferencia_PDS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 14.0 repeats of 'trials_excitadordetransferencia'


# set up handler to look after randomisation of conditions etc
trials_estimulocompuestoinhibidor_PDS = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_estimulocompuestoinhibidor_PDS')
thisExp.addLoop(trials_estimulocompuestoinhibidor_PDS)  # add the loop to the experiment
thisTrials_estimulocompuestoinhibidor_PDS = trials_estimulocompuestoinhibidor_PDS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_estimulocompuestoinhibidor_PDS.rgb)
if thisTrials_estimulocompuestoinhibidor_PDS != None:
    for paramName in thisTrials_estimulocompuestoinhibidor_PDS:
        exec('{} = thisTrials_estimulocompuestoinhibidor_PDS[paramName]'.format(paramName))

for thisTrials_estimulocompuestoinhibidor_PDS in trials_estimulocompuestoinhibidor_PDS:
    currentLoop = trials_estimulocompuestoinhibidor_PDS
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_estimulocompuestoinhibidor_PDS.rgb)
    if thisTrials_estimulocompuestoinhibidor_PDS != None:
        for paramName in thisTrials_estimulocompuestoinhibidor_PDS:
            exec('{} = thisTrials_estimulocompuestoinhibidor_PDS[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ESTIMULO_COMPUESTO_INHIBIDOR" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    slider.reset()
    # keep track of which components have finished
    ESTIMULO_COMPUESTO_INHIBIDORComponents = [text_2, jeje, jiji, slider]
    for thisComponent in ESTIMULO_COMPUESTO_INHIBIDORComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ESTIMULO_COMPUESTO_INHIBIDOR" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                text_2.setAutoDraw(False)
        
        # *jeje* updates
        if jeje.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            jeje.frameNStart = frameN  # exact frame index
            jeje.tStart = t  # local t and not account for scr refresh
            jeje.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jeje, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'jeje.started')
            jeje.setAutoDraw(True)
        if jeje.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jeje.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                jeje.tStop = t  # not accounting for scr refresh
                jeje.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'jeje.stopped')
                jeje.setAutoDraw(False)
        
        # *jiji* updates
        if jiji.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            jiji.frameNStart = frameN  # exact frame index
            jiji.tStart = t  # local t and not account for scr refresh
            jiji.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jiji, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'jiji.started')
            jiji.setAutoDraw(True)
        if jiji.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jiji.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                jiji.tStop = t  # not accounting for scr refresh
                jiji.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'jiji.stopped')
                jiji.setAutoDraw(False)
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider.started')
            slider.setAutoDraw(True)
        if slider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > slider.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                slider.tStop = t  # not accounting for scr refresh
                slider.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider.stopped')
                slider.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ESTIMULO_COMPUESTO_INHIBIDORComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ESTIMULO_COMPUESTO_INHIBIDOR" ---
    for thisComponent in ESTIMULO_COMPUESTO_INHIBIDORComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_estimulocompuestoinhibidor_PDS.addData('slider.response', slider.getRating())
    trials_estimulocompuestoinhibidor_PDS.addData('slider.rt', slider.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "ITI_estimulocompuestoinhibidor_PDS" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ITI_estimulocompuestoinhibidor_PDSComponents = [polygon]
    for thisComponent in ITI_estimulocompuestoinhibidor_PDSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI_estimulocompuestoinhibidor_PDS" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon.started')
            polygon.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_estimulocompuestoinhibidor_PDSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI_estimulocompuestoinhibidor_PDS" ---
    for thisComponent in ITI_estimulocompuestoinhibidor_PDSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI_estimulocompuestoinhibidor_PDS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials_estimulocompuestoinhibidor_PDS'


# set up handler to look after randomisation of conditions etc
trials_estimulocompuestoneutro_PDS = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_estimulocompuestoneutro_PDS')
thisExp.addLoop(trials_estimulocompuestoneutro_PDS)  # add the loop to the experiment
thisTrials_estimulocompuestoneutro_PDS = trials_estimulocompuestoneutro_PDS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_estimulocompuestoneutro_PDS.rgb)
if thisTrials_estimulocompuestoneutro_PDS != None:
    for paramName in thisTrials_estimulocompuestoneutro_PDS:
        exec('{} = thisTrials_estimulocompuestoneutro_PDS[paramName]'.format(paramName))

for thisTrials_estimulocompuestoneutro_PDS in trials_estimulocompuestoneutro_PDS:
    currentLoop = trials_estimulocompuestoneutro_PDS
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_estimulocompuestoneutro_PDS.rgb)
    if thisTrials_estimulocompuestoneutro_PDS != None:
        for paramName in thisTrials_estimulocompuestoneutro_PDS:
            exec('{} = thisTrials_estimulocompuestoneutro_PDS[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ESTIMULO_COMPUESTO_NEUTRO" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    slider_2.reset()
    # keep track of which components have finished
    ESTIMULO_COMPUESTO_NEUTROComponents = [text_3, jojo, juju, slider_2]
    for thisComponent in ESTIMULO_COMPUESTO_NEUTROComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ESTIMULO_COMPUESTO_NEUTRO" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                text_3.setAutoDraw(False)
        
        # *jojo* updates
        if jojo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            jojo.frameNStart = frameN  # exact frame index
            jojo.tStart = t  # local t and not account for scr refresh
            jojo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jojo, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'jojo.started')
            jojo.setAutoDraw(True)
        if jojo.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jojo.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                jojo.tStop = t  # not accounting for scr refresh
                jojo.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'jojo.stopped')
                jojo.setAutoDraw(False)
        
        # *juju* updates
        if juju.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            juju.frameNStart = frameN  # exact frame index
            juju.tStart = t  # local t and not account for scr refresh
            juju.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(juju, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'juju.started')
            juju.setAutoDraw(True)
        if juju.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                juju.tStop = t  # not accounting for scr refresh
                juju.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'juju.stopped')
                juju.setAutoDraw(False)
        
        # *slider_2* updates
        if slider_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            slider_2.frameNStart = frameN  # exact frame index
            slider_2.tStart = t  # local t and not account for scr refresh
            slider_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_2.started')
            slider_2.setAutoDraw(True)
        if slider_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > slider_2.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                slider_2.tStop = t  # not accounting for scr refresh
                slider_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_2.stopped')
                slider_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ESTIMULO_COMPUESTO_NEUTROComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ESTIMULO_COMPUESTO_NEUTRO" ---
    for thisComponent in ESTIMULO_COMPUESTO_NEUTROComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_estimulocompuestoneutro_PDS.addData('slider_2.response', slider_2.getRating())
    trials_estimulocompuestoneutro_PDS.addData('slider_2.rt', slider_2.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "ITI_estimulocompuestoneutro_PDS" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ITI_estimulocompuestoneutro_PDSComponents = [polygon_2]
    for thisComponent in ITI_estimulocompuestoneutro_PDSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI_estimulocompuestoneutro_PDS" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_2.started')
            polygon_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_estimulocompuestoneutro_PDSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI_estimulocompuestoneutro_PDS" ---
    for thisComponent in ITI_estimulocompuestoneutro_PDSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI_estimulocompuestoneutro_PDS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials_estimulocompuestoneutro_PDS'


# set up handler to look after randomisation of conditions etc
trials_estimuloexcitatorio_PDS = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_estimuloexcitatorio_PDS')
thisExp.addLoop(trials_estimuloexcitatorio_PDS)  # add the loop to the experiment
thisTrials_estimuloexcitatorio_PDS = trials_estimuloexcitatorio_PDS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_estimuloexcitatorio_PDS.rgb)
if thisTrials_estimuloexcitatorio_PDS != None:
    for paramName in thisTrials_estimuloexcitatorio_PDS:
        exec('{} = thisTrials_estimuloexcitatorio_PDS[paramName]'.format(paramName))

for thisTrials_estimuloexcitatorio_PDS in trials_estimuloexcitatorio_PDS:
    currentLoop = trials_estimuloexcitatorio_PDS
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_estimuloexcitatorio_PDS.rgb)
    if thisTrials_estimuloexcitatorio_PDS != None:
        for paramName in thisTrials_estimuloexcitatorio_PDS:
            exec('{} = thisTrials_estimuloexcitatorio_PDS[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ESTIMULO_EXCITATORIO_PDS" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    slider_3.reset()
    ei.setImage(EI_FOTO)
    eisonido.setSound(EI_SONIDO, secs=0.7, hamming=True)
    eisonido.setVolume(1.0, log=False)
    # keep track of which components have finished
    ESTIMULO_EXCITATORIO_PDSComponents = [text_4, joasjoas, slider_3, ei, eisonido]
    for thisComponent in ESTIMULO_EXCITATORIO_PDSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ESTIMULO_EXCITATORIO_PDS" ---
    while continueRoutine and routineTimer.getTime() < 4.8:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.stopped')
                text_4.setAutoDraw(False)
        
        # *joasjoas* updates
        if joasjoas.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            joasjoas.frameNStart = frameN  # exact frame index
            joasjoas.tStart = t  # local t and not account for scr refresh
            joasjoas.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(joasjoas, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'joasjoas.started')
            joasjoas.setAutoDraw(True)
        if joasjoas.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > joasjoas.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                joasjoas.tStop = t  # not accounting for scr refresh
                joasjoas.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'joasjoas.stopped')
                joasjoas.setAutoDraw(False)
        
        # *slider_3* updates
        if slider_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            slider_3.frameNStart = frameN  # exact frame index
            slider_3.tStart = t  # local t and not account for scr refresh
            slider_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_3.started')
            slider_3.setAutoDraw(True)
        if slider_3.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                slider_3.tStop = t  # not accounting for scr refresh
                slider_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_3.stopped')
                slider_3.setAutoDraw(False)
        
        # *ei* updates
        if ei.status == NOT_STARTED and tThisFlip >= 4.1-frameTolerance:
            # keep track of start time/frame for later
            ei.frameNStart = frameN  # exact frame index
            ei.tStart = t  # local t and not account for scr refresh
            ei.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ei, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ei.started')
            ei.setAutoDraw(True)
        if ei.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ei.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                ei.tStop = t  # not accounting for scr refresh
                ei.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ei.stopped')
                ei.setAutoDraw(False)
        # start/stop eisonido
        if eisonido.status == NOT_STARTED and tThisFlip >= 4.1-frameTolerance:
            # keep track of start time/frame for later
            eisonido.frameNStart = frameN  # exact frame index
            eisonido.tStart = t  # local t and not account for scr refresh
            eisonido.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('eisonido.started', tThisFlipGlobal)
            eisonido.play(when=win)  # sync with win flip
        if eisonido.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eisonido.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                eisonido.tStop = t  # not accounting for scr refresh
                eisonido.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eisonido.stopped')
                eisonido.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ESTIMULO_EXCITATORIO_PDSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ESTIMULO_EXCITATORIO_PDS" ---
    for thisComponent in ESTIMULO_EXCITATORIO_PDSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_estimuloexcitatorio_PDS.addData('slider_3.response', slider_3.getRating())
    trials_estimuloexcitatorio_PDS.addData('slider_3.rt', slider_3.getRT())
    eisonido.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.800000)
    
    # --- Prepare to start Routine "ITI_estimuloexcitatorio_PDS" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ITI_estimuloexcitatorio_PDSComponents = [polygon_5]
    for thisComponent in ITI_estimuloexcitatorio_PDSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI_estimuloexcitatorio_PDS" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_5* updates
        if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.tStart = t  # local t and not account for scr refresh
            polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_5.started')
            polygon_5.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_estimuloexcitatorio_PDSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI_estimuloexcitatorio_PDS" ---
    for thisComponent in ITI_estimuloexcitatorio_PDSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI_estimuloexcitatorio_PDS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials_estimuloexcitatorio_PDS'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

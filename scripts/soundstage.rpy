init python:
    import math
    af = renpy.audio.filter
    
    def soundstage(pan, distance, channel='music', volume_proportion=1.0, lowpass_proportion=1.0, reverb_proportion=1.0, pan_delay=0., volume_delay=0., lowpass_frequency=22000):
        """
        Dynamically adjusts audio properties based on pan and distance to simulate a 3D soundstage.
        
        Args:
            pan (float): The stereo panning value (typically between -1.0 and 1.0).
            distance (float): The distance of the sound source from the listener (must be between 0 and 100).
            channel (str): The audio channel to apply the effects to. Defaults to 'music'.
            volume_proportion (float): Clamped ratio for overall volume adjustment (0.0 to 1.0).
            lowpass_proportion (float): Clamped ratio for the lowpass filter effect (0.0 to 1.0).
            reverb_proportion (float): Clamped ratio for the reverb effect (0.0 to 1.0).
            pan_delay (float): The time delay in seconds for the panning transition. Defaults to 0.
            volume_delay (float): The time delay in seconds for the volume transition. Defaults to 0.
            lowpass_frequency (int): The frequency value that it gives to the af.Lowpass().
            
        Raises:
            ValueError: If distance is not within the range [0, 100].
        """
        # Clamp proportion arguments to ensure they stay within the valid 0.0 to 1.0 range
        volume_proportion = max(0.0, min(1.0, volume_proportion))
        lowpass_proportion = max(0.0, min(1.0, lowpass_proportion))
        reverb_proportion = max(0.0, min(1.0, reverb_proportion))
        
        # Apply audio environmental effects if distance is valid
        if 0 <= distance <= 100:
            # Set the stereo position
            renpy.music.set_pan(pan=pan, delay=pan_delay, channel=channel)
            
            # Calculate and set volume attenuation using an inverse-square law approximation based on distance
            renpy.music.set_volume(math.pow((100-distance)/100.0 / volume_proportion, 2), delay=volume_delay, channel=channel)
            
            # Apply dynamic audio filters: Lowpass cutoff frequency decreases and Reverb wetness increases as distance grows
            renpy.music.set_audio_filter(channel=channel, audio_filter=[af.Lowpass(lowpass_frequency-distance*210*lowpass_proportion, 0), af.Reverb(wet=(distance / 100) * reverb_proportion ** 2, dry=1 / reverb_proportion / (1 + 0.002 * (distance ** 2)))], replace=True)
        else:
            raise ValueError("Distance must be between 0 and 100.")

screen soundstage_control:
    default distance = 0
    default pan = 0
    text "Distance: [distance]":
        xalign 0.5
        yalign 0.4
    vbar:
        value ScreenVariableValue("distance", min=0, max=100)
        xpos int((pan + 100) * 1910 / 200)
        yalign 0.1
        ysize 650
        changed soundstage(pan/100, distance, volume_delay=0.05, pan_delay=0.05, volume_proportion=0.5, lowpass_proportion=0.5, reverb_proportion=0.5)
    text "Pan: [pan]":
        xalign 0.5
        yalign 0.6
    bar:
        value ScreenVariableValue("pan", min=-100, max=100, step=0.01)
        xsize 1910
        xalign 0.5
        yalign 0.7
        changed soundstage(pan/100, distance, volume_delay=0.05, pan_delay=0.05, volume_proportion=0.5, lowpass_proportion=0.5, reverb_proportion=0.5)
# those_pesky_satellites

### ========== Key Terms ==========

- Epoch: Precise date and time at which the satellite readings have been taken. Data becomes unreliable if epoch is outside of 14 days 
- Eccentricity: Deviation from a perfect sphere; 0 is a perfect circle while 1 is a line
- Mean Motion: Number of orbits per day
- Inclination: Tilt of the orbital plane relative to Earth's equator
- RA: Right Ascension; orientation of the orbital plane around the Earth
- Arg of Pericenter: Orientation of the orbit's closest point to Earth
- Mean Anomaly: Satellite's position along its orbit at the Epoch
- BSTAR: Atmospheric Drag parameter used by the propagator 
- Mean_Motion_DOT: Rate of change of mean motion
- Mean_Motion_DDOT: Rate of change of Mean_Motion_DOT; Second derivative of mean of motion

To calculate the orbital position, we only need a few of these. The __epoch__ is the timestamp that other orbital parameters reference, and thus is important as a baseline of all measurements. We must propagate the orbit forward from this orbit to gather the current orbital position.

The __Mean Motion__ is the satellite's average number of revolutions per day, which can be converted into orbital period with the equation: $period.minutes = 1440 / mean.motion$. 

The __eccentricity__ is important to calculate how much the orbit deviates from a perfect circle.

__Inclination__ tells us the angle between the satellite's orbital plane and the Earth's equatorial plane. 0 degrees and 180 degrees mark equatorial orbits in opposite directions, while 90 degrees represents a polar orbit.

The __Right Ascension of the Ascending Node (RAAN)__, represented by RA_OF_ASC_NODE, is the point at which the satellite crosses the Earth's equatorial plane while moving upwards from South -> North. We use these last two components to define the rotation/orientation of the orbital plane around Earth.

Argument Pericenter - where orbits closest point to Earth (perigee) is in orbital plane; orientation of the ellipse inside its orbital plane

Mean Anomaly - satellite orbital position at epoch.
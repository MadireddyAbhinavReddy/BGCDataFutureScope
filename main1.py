import streamlit as st
import pandas as pd
import xarray as xr
import numpy as np

def show_bgc_argo_page():
    """
    Creates and displays the BGC-ARGO data overview page.
    """
    st.set_page_config(layout="wide")

    st.title("🧪 BGC-ARGO: Monitoring the Ocean's Biological Pulse")
    st.markdown("""
    While standard ARGO floats reveal the ocean's physical state (temperature, salinity), **Biogeochemical (BGC) ARGO floats** dive deeper. They are equipped with advanced sensors to measure the ocean's health, chemistry, and the very building blocks of marine life.

    This page provides an overview of BGC-ARGO data and how you can use it in **FloatChat**.
    """)

    # --- 1. Key BGC Parameters ---
    st.header("🔬 Key Parameters Measured by BGC Floats")
    st.markdown("BGC floats measure several crucial variables beyond the standard CTD (Conductivity, Temperature, Depth):")

    col1, col2 = st.columns(2)
    with col1:
        st.info(f"""
        - **Dissolved Oxygen ($O_2$)**: Essential for marine life. Tracks oxygen minimum zones and overall ocean health.
        - **Nitrate ($NO_3^-$)**: A primary nutrient for phytoplankton, acting as a fertilizer for the ocean's base food web.
        - **pH**: Measures ocean acidity, providing vital data on the impacts of atmospheric $CO_2$ absorption.
        """)
    with col2:
        st.warning(f"""
        - **Chlorophyll-a (CHLA)**: The primary pigment in phytoplankton. It's a direct proxy for algal biomass.
        - **Backscattering (BBP)**: Measures suspended particles in the water, used to estimate Particulate Organic Carbon (POC).
        - **Downwelling Irradiance (DOWN_IRRADIANCE)**: Measures sunlight penetration, key for photosynthesis.
        """)
    st.image("https://i.imgur.com/uR1B3b4.jpeg", caption="", use_column_width=True)


    # --- 2. Accessing & Processing BGC Data ---
    st.header("⚙️ Accessing and Processing the Data")
    st.markdown("""
    Accessing BGC data is similar to core ARGO data, typically through the same data centers (GDACs). The key difference is in the NetCDF files, which contain many more variables. You can identify BGC profiles by looking for files prefixed with `B` or by checking for biogeochemical parameter names.

    **`xarray`** remains the perfect tool for this job.
    """)

    st.subheader("Example: Loading a BGC NetCDF File")
    st.code("""
import xarray as xr

# Load a BGC-ARGO NetCDF file
# Note: BGC files often have more variables and dimensions
bgc_ds = xr.open_dataset("path/to/your/BGC_float_data.nc")

# Print the variables to see what's inside
print(bgc_ds.variables)
# You'll see variables like 'DOXY', 'CHLA', 'NITRATE', 'PH_IN_SITU_TOTAL', etc.

# Select a specific biogeochemical profile
chlorophyll_profile = bgc_ds['CHLA'].isel(N_PROF=0)
oxygen_profile = bgc_ds['DOXY'].isel(N_PROF=0)

print(chlorophyll_profile)
    """, language="python")


    # --- 3. Applications and Scientific Impact ---
    st.header("🌎 Why BGC Data is a Game-Changer")
    st.markdown("This data enables us to answer critical questions about the health of our planet.")

    with st.expander("Tracking Ocean Deoxygenation"):
        st.markdown("""
        By providing widespread, real-time measurements of dissolved oxygen, BGC floats help scientists monitor the expansion of Oxygen Minimum Zones (OMZs), which are areas lethal to most marine life.
        """)

    with st.expander("Understanding the Biological Carbon Pump"):
        st.markdown("""
        Phytoplankton absorb $CO_2$ during photosynthesis. When they die, some of this carbon sinks to the deep ocean, a process called the biological carbon pump. BGC data (especially Nitrate, CHLA, and BBP) allows us to quantify this critical climate-regulating mechanism.
        """)

    with st.expander("Monitoring Phytoplankton Blooms"):
        st.markdown("""
        Chlorophyll-a profiles show the vertical structure of phytoplankton blooms. This is a massive improvement over satellites, which can only see the surface. With BGC floats, we can see if a bloom is just a thin surface layer or a deep, thriving ecosystem.
        """)

    st.subheader("Example Visualization: A Typical Chlorophyll Profile")
    st.markdown("Below is a sample plot showing how Chlorophyll-a concentration is often highest near the surface (in the 'photic zone') and decreases with depth.")

    # Create synthetic data for a chlorophyll profile
    depth = np.arange(0, 500, 10)
    # Simulate a subsurface chlorophyll maximum
    chl_a = (np.exp(-(depth - 100)**2 / (2 * 40**2)) * 1.5 + np.random.rand(len(depth)) * 0.1)
    profile_df = pd.DataFrame({
        "Chlorophyll-a (mg/m³)" : chl_a,
        "Depth (m)": -depth # Use negative depth for conventional ocean plots
    }).set_index("Depth (m)")

    st.line_chart(profile_df)


if __name__ == '__main__':
    show_bgc_argo_page()
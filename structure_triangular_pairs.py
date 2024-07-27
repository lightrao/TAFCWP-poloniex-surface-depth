def structure_triangular_pairs(coin_list):
    # Declare Variables
    triangular_pairs_list = []
    remove_duplicates_list = set()
    pairs_list = coin_list.copy()

    # Get Pair A
    for pair_a in pairs_list:
        a_base, a_quote = pair_a.split("_")

        # Get Pair B
        for pair_b in pairs_list:
            if pair_b == pair_a:
                continue

            b_base, b_quote = pair_b.split("_")

            # Check Pair B
            if b_base in [a_base, a_quote] or b_quote in [a_base, a_quote]:
                # Get Pair C
                for pair_c in pairs_list:
                    if pair_c in [pair_a, pair_b]:
                        continue

                    c_base, c_quote = pair_c.split("_")

                    # Determine if there's a triangular match
                    pair_box = [a_base, a_quote, b_base, b_quote, c_base, c_quote]
                    if (
                        pair_box.count(c_base) == 2
                        and pair_box.count(c_quote) == 2
                        and c_base != c_quote
                    ):
                        combined = f"{pair_a},{pair_b},{pair_c}"
                        unique_item = "".join(sorted([pair_a, pair_b, pair_c]))

                        if unique_item not in remove_duplicates_list:
                            match_dict = {
                                "a_base": a_base,
                                "b_base": b_base,
                                "c_base": c_base,
                                "a_quote": a_quote,
                                "b_quote": b_quote,
                                "c_quote": c_quote,
                                "pair_a": pair_a,
                                "pair_b": pair_b,
                                "pair_c": pair_c,
                                "combined": combined,
                            }
                            triangular_pairs_list.append(match_dict)
                            remove_duplicates_list.add(unique_item)

    print(len(triangular_pairs_list))
    print(triangular_pairs_list[:20])
    return triangular_pairs_list


# Example usage
coin_list = [
    "BTS_BTC",
    "DASH_BTC",
    "DOGE_BTC",
    "LTC_BTC",
    "XLM_BTC",
    "XEM_BTC",
    "XMR_BTC",
    "XRP_BTC",
    "BTC_USDT",
    "DASH_USDT",
    "LTC_USDT",
    "XLM_USDT",
    "XMR_USDT",
    "XRP_USDT",
    "ETH_BTC",
    "ETH_USDT",
    "SC_BTC",
    "DCR_BTC",
    "LSK_BTC",
    "STEEM_BTC",
    "ETC_BTC",
    "ETC_ETH",
    "ETC_USDT",
    "ARDR_BTC",
    "ZEC_BTC",
    "ZEC_ETH",
    "ZEC_USDT",
    "ZRX_BTC",
    "ZRX_ETH",
    "CVC_BTC",
    "GAS_BTC",
    "STORJ_BTC",
    "EOS_BTC",
    "EOS_ETH",
    "EOS_USDT",
    "SNT_BTC",
    "BAT_BTC",
    "BAT_USDT",
    "LOOM_BTC",
    "DOGE_USDT",
    "LSK_USDT",
    "SC_USDT",
    "ZRX_USDT",
    "QTUM_BTC",
    "QTUM_USDT",
    "BTC_USDC",
    "ETH_USDC",
    "USDT_USDC",
    "MANA_BTC",
    "MANA_USDT",
    "BCHSV_BTC",
    "XRP_USDC",
    "LTC_USDC",
    "POLY_BTC",
    "ATOM_BTC",
    "ATOM_USDT",
    "BCHSV_USDT",
    "TRX_BTC",
    "TRX_USDC",
    "TRX_USDT",
    "ETH_TRX",
    "XRP_TRX",
    "BTT_USDT",
    "BTT_TRX",
    "WIN_USDT",
    "WIN_TRX",
    "STEEM_TRX",
    "LINK_BTC",
    "LINK_TRX",
    "XTZ_USDT",
    "USDJ_USDT",
    "SNX_BTC",
    "SNX_USDT",
    "SNX_TRX",
    "MATIC_BTC",
    "MATIC_USDT",
    "MATIC_TRX",
    "MKR_BTC",
    "MKR_USDT",
    "DAI_USDT",
    "NEO_BTC",
    "NEO_USDT",
    "SWFTC_BTC",
    "SWFTC_USDT",
    "JST_USDT",
    "JST_TRX",
    "STEEM_USDT",
    "LINK_USDT",
    "AVA_BTC",
    "AVA_USDT",
    "AVA_TRX",
    "XRPBULL_USDT",
    "CHR_BTC",
    "CHR_USDT",
    "BTC_BNB",
    "BNB_USDT",
    "BNB_TRX",
    "MDT_BTC",
    "MDT_USDT",
    "MDT_TRX",
    "COMP_USDT",
    "COMP_ETH",
    "REN_USDT",
    "LRC_BTC",
    "LRC_USDT",
    "BAL_USDT",
    "WRX_USDT",
    "WRX_TRX",
    "SXP_BTC",
    "SXP_USDT",
    "YFI_USDT",
    "STPT_USDT",
    "UMA_USDT",
    "RING_USDT",
    "SWAP_USDT",
    "GEEQ_USDT",
    "BAND_USDT",
    "DOS_USDT",
    "DIA_USDT",
    "TRB_USDT",
    "DEXT_USDT",
    "CRV_USDT",
    "OM_USDT",
    "OCEAN_USDT",
    "SWINGBY_USDT",
    "PRQ_USDT",
    "DOT_USDT",
    "RSR_USDT",
    "WNXM_USDT",
    "FCT2_USDT",
    "SUSHI_USDT",
    "YFII_USDT",
    "FUND_USDT",
    "FUND_TRX",
    "FUND_BTC",
    "AKRO_USDT",
    "UNI_USDT",
    "CVP_USDT",
    "GHST_USDT",
    "RARI_USDT",
    "AMP_BTC",
    "AMP_USDT",
    "SAND_BTC",
    "SAND_USDT",
    "POLS_USDT",
    "AAVE_BTC",
    "AAVE_USDT",
    "CVT_BTC",
    "CVT_USDT",
    "INJ_BTC",
    "INJ_USDT",
    "BCH_BTC",
    "BCH_USDT",
    "SENSO_USDT",
    "KP3R_USDT",
    "GLM_BTC",
    "GLM_USDT",
    "ZLOT_USDT",
    "FRONT_BTC",
    "FRONT_USDT",
    "API3_USDT",
    "BADGER_USDT",
    "FARM_USDT",
    "DOT_BTC",
    "GRT_USDT",
    "ESD_USDT",
    "ONEINCH_USDT",
    "REEF_USDT",
    "LON_USDT",
    "TRU_USDT",
    "BOND_USDT",
    "TUSD_USDT",
    "WETH_USDT",
    "TRU_BTC",
    "FTT_USDT",
    "LPT_USDT",
    "ALPHA_USDT",
    "RNDR_USDT",
    "KCS_USDT",
    "FIL_BTC",
    "FIL_USDT",
    "XYM_BTC",
    "XYM_USDT",
    "LIVE_USDT",
    "SHIB_USDT",
    "AKITA_USDT",
    "KLV_USDT",
    "LQTY_USDT",
    "DEGO_USDT",
    "ELON_USDT",
    "QUICK_USDT",
    "MVL_USDT",
    "NFT_USDT",
    "NFT_TRX",
    "HT_USDT",
    "CTSI_USDT",
    "RLC_USDT",
    "ERSDL_USDT",
    "RUNE_USDT",
    "KISHU_TRX",
    "GTC_USDT",
    "OKB_USDT",
    "SUN_USDT",
    "XEC_USDT",
    "CAKE_USDT",
    "XVS_USDT",
    "BURGER_USDT",
    "AXS_USDT",
    "ALPACA_USDT",
    "C98_USDT",
    "PERP_USDT",
    "ACH1_USDT",
    "CLV_USDT",
    "YGG_USDT",
    "ALICE_USDT",
    "AUDIO_USDT",
    "BNB_USDC",
    "MBOX_USDT",
    "AGLD_USDT",
    "BTT_USDC",
    "XEM_USDT",
    "DYDX_USDT",
    "XCAD_USDT",
    "GALA_USDT",
    "LDO_USDT",
    "BTRST_USDT",
    "FLOKI_USDT",
    "TOKE_USDT",
    "WNCG_USDT",
    "MLN_USDT",
    "WOO_USDT",
    "ENJ_USDT",
    "CHZ_USDT",
    "SLP_USDT",
    "OGN_USDT",
    "PLA_USDT",
    "TLM_USDT",
    "SUPER_USDT",
    "ILV_USDT",
    "ERN_USDT",
    "SPELL_USDT",
    "EFI_USDT",
    "RACA_USDT",
    "AVAX_USDT",
    "GMEE_USDT",
    "CVX_USDT",
    "AVAX_BTC",
    "ENS_USDT",
    "IMX_USDT",
    "GN_USDT",
    "SAITAMA_USDT",
    "BOBA_USDT",
    "POLYDOGE_USDT",
    "FXS_USDT",
    "DYP_USDT",
    "TRIBE_USDT",
    "SOL_USDT",
    "SOL_BTC",
    "DORA_USDT",
    "ORCA_USDT",
    "PEOPLE_USDT",
    "PSP_USDT",
    "NEXO_USDT",
    "FTM_USDT",
    "BNX_USDT",
    "QI_USDT",
    "ADA_USDT",
    "REQ_USDT",
    "SAMO_USDT",
    "ATLAS_USDT",
    "POLIS_USDT",
    "FIDA_USDT",
    "BICO_USDT",
    "GODS_USDT",
    "RBN_USDT",
    "PYR_USDT",
    "HIGH_USDT",
    "VOXEL_USDT",
    "ADA_BTC",
    "CTC_USDT",
    "METIS_USDT",
    "OOKI_USDT",
    "LOOKS_USDT",
    "FTM_BTC",
    "SHPING_USDT",
    "LOKA_USDT",
    "VRA_USDT",
    "SUKU_USDT",
    "NCT_USDT",
    "HUNT_USDT",
    "TITAN_USDT",
    "UMEE_USDT",
    "ALPINE_USDT",
    "GMT_USDT",
    "AERGO_USDT",
    "APE_USDT",
    "NVIR_USDT",
    "STG_USDT",
    "CULT_USDT",
    "KSM_USDT",
    "ZELIX_USDT",
    "NYM_USDT",
    "DAR_USDT",
    "USDD_USDT",
    "G_USDT",
    "FITFI_USDT",
    "EPX_USDT",
    "BTC_USDD",
    "ETH_USDD",
    "TRX_USDD",
    "BTT_USDD",
    "JST_USDD",
    "WIN_USDD",
    "SUN_USDD",
    "XRP_USDD",
    "LTC_USDD",
    "DOT_USDD",
    "XCN_USDT",
    "FRAX_USDT",
    "KUB_USDT",
    "WLKN_USDT",
    "BNT_USDT",
    "LOOM_USDT",
    "KNC_USDT",
    "SNT_USDT",
    "LUNA_USDT",
    "LUNC_USDT",
    "ETHW_USDT",
    "ETHW_ETH",
    "POLOTEST2_POLOTEST1",
    "POLOTEST3_POLOTEST4",
    "POLOTEST2_POLOTEST4",
    "POLOTEST2_POLOTEST3",
    "POLOTEST1_POLOTEST4",
    "POLOTEST1_POLOTEST3",
    "POLOTEST1_POLOTEST2",
    "SANTOS_USDT",
    "NMR_USDT",
    "CVC_USDT",
    "STORJ_USDT",
    "OMG_USDT",
    "ETHF_USDT",
    "DC_USDT",
    "SSV_USDT",
    "APX_USDT",
    "AFC_USDT",
    "CITY_USDT",
    "ZBCN_USDT",
    "XEN_USDT",
    "BTS_USDT",
    "DCR_USDT",
    "ARDR_USDT",
    "GAS_USDT",
    "HFT_USDT",
    "OP_USDT",
    "GMX_USDT",
    "NEAR_USDT",
    "ACM_USDT",
    "JUV_USDT",
    "ASR_USDT",
    "PSG_USDT",
    "TONOLD_USDT",
    "MASK_USDT",
    "ARG_USDT",
    "POR_USDT",
    "APT_USDT",
    "VELO_USDT",
    "VINU_USDT",
    "BAR_USDT",
    "ATM_USDT",
    "CEL_USDT",
    "BITCI_USDT",
    "BFT_USDT",
    "VGX_USDT",
    "PORTO_USDT",
    "LAZIO_USDT",
    "FLR_USDT",
    "UT_USDT",
    "TRR_USDT",
    "BONK_USDT",
    "OG_USDT",
    "VOLT_USDT",
    "DUSK_USDT",
    "GNS_USDT",
    "SUDO_USDT",
    "IGU_USDT",
    "BABYDOGE_USDT",
    "KON_USDT",
    "ICP_USDT",
    "BLUR_USDT",
    "CARMIN_USDT",
    "FET_USDT",
    "CORE_USDT",
    "IMGNAI_USDT",
    "AGIX_USDT",
    "RPL_USDT",
    "TSUKA_USDT",
    "FACTR_USDT",
    "GPT_USDT",
    "BONE_USDT",
    "ALI_USDT",
    "SDAO_USDT",
    "GFT_USDT",
    "LOGT_USDT",
    "RDNT_USDT",
    "ROCK_USDT",
    "RIF_USDT",
    "BRISE_USDT",
    "POOLX_USDT",
    "PAW_USDT",
    "PENDLE_USDT",
    "ID_USDT",
    "ARB_USDT",
    "RIO_USDT",
    "RUG_USDT",
    "BOBOETH_USDT",
    "BABYPEPE_USDT",
    "CGPT_USDT",
    "CHAD_USDT",
    "WOJAK_USDT",
    "AGI_USDT",
    "PEPE_USDT",
    "AIDOGE_USDT",
    "LZM_USDT",
    "WIFI_USDT",
    "RMV_USDT",
    "POOH_USDT",
    "TURBO_USDT",
    "POGAI_USDT",
    "FLOKICEO_USDT",
    "SUI_USDT",
    "BOB_USDT",
    "SOV_USDT",
    "SOLO_USDT",
    "COREUM_USDT",
    "CAPO_USDT",
    "BEN_USDT",
    "KING_USDT",
    "SPONGE_USDT",
    "RFD_USDT",
    "LIMO_USDT",
    "OGGY_USDT",
    "DONS_USDT",
    "PEPEAI_USDT",
    "SIMPSON_USDT",
    "HARRY_USDT",
    "LADYS_USDT",
    "MONG_USDT",
    "LBR_USDT",
    "AMC_USDT",
    "MIDWIT_USDT",
    "DMT_USDT",
    "BNBDADDY_USDT",
    "BIG_USDT",
    "LVL_USDT",
    "LOVESNOOPY_USDT",
    "INU_USDT",
    "FERC_USDT",
    "STT_USDT",
    "JESUS_USDT",
    "PEPE2_USDT",
    "MMT_USDT",
    "UPP_USDT",
    "TOKAMAK_USDT",
    "MPWR_USDT",
    "MAV_USDT",
    "TITTY_USDT",
    "L_USDT",
    "TOMI_USDT",
    "OX_USDT",
    "ORDI_USDT",
    "VMPX_USDT",
    "PLANET_USDT",
    "VOW_USDT",
    "UNIBOT_USDT",
    "HOPPY_USDT",
    "OSMO_USDT",
    "WSTUSDT_USDT",
    "JARED_USDT",
    "HAM_USDT",
    "PEPE20_USDT",
    "SHIB2_USDT",
    "DOGE2_USDT",
    "BSWAP_USDT",
    "TOSHI_USDT",
    "WINR_USDT",
    "PNDC_USDT",
    "RLB_USDT",
    "XTOKEN_USDT",
    "WLD_USDT",
    "X_USDT",
    "BAD_USDT",
    "HAMS_USDT",
    "MOG_USDT",
    "LOOT_USDT",
    "SG_USDT",
    "BTP_USDT",
    "AITECH_USDT",
    "SHIA_USDT",
    "LL_USDT",
    "FOOM_USDT",
    "AIMBOT_USDT",
    "STMX_USDT",
    "GMMT_USDT",
    "APX1_USDT",
    "SMURFCAT_USDT",
    "SATS_USDT",
    "HIFI_USDT",
    "VEXT_USDT",
    "BANANA_USDT",
    "CCROWD_USDT",
    "DOBO_USDT",
    "DORKL_USDT",
    "ETHPEPE2_USDT",
    "TISM_USDT",
    "ETF_USDT",
    "NAKA_USDT",
    "NLC_USDT",
    "SIX_USDT",
    "APU_USDT",
    "REKT2_USDT",
    "BIGTIME_USDT",
    "OPOS_USDT",
    "RATS_USDT",
    "PAAL_USDT",
    "GROK_USDT",
    "VAULT_USDT",
    "KAS_USDT",
    "AMO_USDT",
    "MEMELAND_USDT",
    "CRE_USDT",
    "JTO_USDT",
    "FTN_USDT",
    "BLOX_USDT",
    "IOT_USDT",
    "HNT_USDT",
    "MOBILE_USDT",
    "MYRO_USDT",
    "PMG_USDT",
    "MND_USDT",
    "BYTE_USDT",
    "FLIP_USDT",
    "GEC_USDT",
    "STX_USDT",
    "MNDE_USDT",
    "TURT_USDT",
    "BSSB_USDT",
    "MUBI_USDT",
    "NFP_USDT",
    "BFIC_USDT",
    "DOVI_USDT",
    "XPE_USDT",
    "SEEU_USDT",
    "BOO_USDT",
    "ANALOS_USDT",
    "KNOB_USDT",
    "AI_USDT",
    "PONKE_USDT",
    "ACE_USDT",
    "ZERO_USDT",
    "SILLY_USDT",
    "SPEERO_USDT",
    "COM_USDT",
    "RAY_USDT",
    "RDEX_USDT",
    "CSAS_USDT",
    "DSWP_USDT",
    "MMSS_USDT",
    "LONG1_USDT",
    "SHDW1_USDT",
    "ZKF_USDT",
    "COQ_USDT",
    "USEDCAR_USDT",
    "GUAC_USDT",
    "BSSB1_USDT",
    "ORDS_USDT",
    "AI1_USDT",
    "FERRET_USDT",
    "MUSKX_USDT",
    "MYRA_USDT",
    "DACC_USDT",
    "ZUZALU_USDT",
    "EGG_USDT",
    "BOZO_USDT",
    "TRAC_USDT",
    "RSTK_USDT",
    "FENTANYL_USDT",
    "SFARM_USDT",
    "TROLL_USDT",
    "ROUP_USDT",
    "WIF_USDT",
    "HTX_USDT",
    "SBF_USDT",
    "BFI_USDT",
    "SMILEY_USDT",
    "SAVM_USDT",
    "ONDO_USDT",
    "CROCCAT_USDT",
    "MOCKJUP_USDT",
    "EACC_USDT",
    "GENESIS_USDT",
    "WYNN_USDT",
    "BAKE_USDT",
    "TRUMP_USDT",
    "CHOW_USDT",
    "SPOODY_USDT",
    "HONK_USDT",
    "GTAI_USDT",
    "ALT_USDT",
    "FOMO_USDT",
    "LAMBOSOL_USDT",
    "INS_USDT",
    "DOGWIFFORK_USDT",
    "HODLSOL_USDT",
    "JUP_USDT",
    "SSB_USDT",
    "MEOW_USDT",
    "TELEPATHY_USDT",
    "WEN_USDT",
    "GME_USDT",
    "VEC_USDT",
    "PEAS_USDT",
    "SNOW_USDT",
    "PONK_USDT",
    "CHINU_USDT",
    "AERODROME_USDT",
    "PIXEL_USDT",
    "STRK_USDT",
    "JIVA_USDT",
    "SORA_USDT",
    "MAVIA_USDT",
    "SPYRO_USDT",
    "NAVX_USDT",
    "WHALES_USDT",
    "LMWR_USDT",
    "BFICGOLD_BFIC",
    "YES_USDT",
    "GMEONETH_USDT",
    "SQUIDSOL_USDT",
    "FART_USDT",
    "ZETA_USDT",
    "PEBO_USDT",
    "AC_USDT",
    "DZHV_USDT",
    "TREMP_USDT",
    "BIF_USDT",
    "SHU_USDT",
    "TBANK_USDT",
    "ICENETWORK_USDT",
    "MOBY_USDT",
    "CHAT_USDT",
    "ML_USDT",
    "BENDOG_USDT",
    "BEOBLE_USDT",
    "PORK_USDT",
    "NADA_USDT",
    "XPET_USDT",
    "KLIMA_USDT",
    "CLOSEDAI_USDT",
    "BRETT_USDT",
    "PENG_USDT",
    "OPSEC_USDT",
    "UPDOG_USDT",
    "PORTAL_USDT",
    "ALVA_USDT",
    "HEMULE_USDT",
    "CAF_USDT",
    "FORK_USDT",
    "SOLCHAT_USDT",
    "POPCAT_USDT",
    "RFKJ_USDT",
    "TRUMP1_USDT",
    "TYT_USDT",
    "NEVER_USDT",
    "BOME_USDT",
    "AEVO_USDT",
    "MUMU_USDT",
    "OETH_ETH",
    "OETH_USDT",
    "PRISMA_USDT",
    "BFICGOLD_USDT",
    "SYNC_USDT",
    "FAIR_USDT",
    "WTAO_USDT",
    "CLD_USDT",
    "GPU_USDT",
    "DEPD_USDT",
    "MOZ_USDT",
    "BVM_USDT",
    "SCA_USDT",
    "NOCHILL_USDT",
    "NAP_USDT",
    "DUPE_USDT",
    "WEETH_ETH",
    "SAFEMOON_USDT",
    "IDK_USDT",
    "SLERF_USDT",
    "GTOP_USDT",
    "ETHFI_USDT",
    "POGAISOL_USDT",
    "BINU_USDT",
    "ACRIA_USDT",
    "MOROS_USDT",
    "PORTNOY_USDT",
    "ANDYSOL_USDT",
    "PANDA_USDT",
    "PIPI_USDT",
    "COME_USDT",
    "SHROOM_USDT",
    "FIRE_USDT",
    "LOOMSOL_USDT",
    "NGL_USDT",
    "ENTS_USDT",
    "DEGEN_USDT",
    "PNUT_USDT",
    "BRIUN_USDT",
    "NORMIEOLD_USDT",
    "PRIME_USDT",
    "GRIMACE_USDT",
    "SMOLE_USDT",
    "KERMIT_USDT",
    "MAIL_USDT",
    "FINK_USDT",
    "FOMOBASE_USDT",
    "DOGINME_USDT",
    "SORABTC_USDT",
    "LIME_USDT",
    "MEW_USDT",
    "REX_USDT",
    "PUNDU_USDT",
    "BASEDAI_USDT",
    "BODEN_USDT",
    "PUMP_USDT",
    "BENJI_USDT",
    "DWIFC_USDT",
    "CWIF_USDT",
    "VENOM_USDT",
    "MOGGO_USDT",
    "DOG_USDT",
    "SHOL_USDT",
    "SHIV_USDT",
    "SBFSOL_USDT",
    "IXS_USDT",
    "TPU_USDT",
    "NEURA_USDT",
    "ARCX_USDT",
    "CSWAP_USDT",
    "ROOST_USDT",
    "GRUMPY_USDT",
    "DAW_USDT",
    "ALU_USDT",
    "SCALE_USDT",
    "SPCT_USDT",
    "YAI_USDT",
    "BLERF_USDT",
    "HASHAI_USDT",
    "DEAI_USDT",
    "BUB_USDT",
    "HIGHER_USDT",
    "TYBG_USDT",
    "LYTE_USDT",
    "HOBBES_USDT",
    "BSHIB_USDT",
    "ENA_USDT",
    "CATINO_USDT",
    "MFER_USDT",
    "STOS_USDT",
    "T_USDT",
    "PUPS_USDT",
    "APUFF_USDT",
    "USDE_USDT",
    "XEROAI_USDT",
    "ANDYETH_USDT",
    "RIVUS_USDT",
    "BORED_USDT",
    "LOCK_USDT",
    "SHARKCAT_USDT",
    "CHKN_USDT",
    "NAO_USDT",
    "JUSTANEGG_USDT",
    "O4DX_USDT",
    "TNSR_USDT",
    "X314_USDT",
    "FRENPET_USDT",
    "KAI_USDT",
    "COINYE_USDT",
    "ASTO_USDT",
    "BASEFOMO_USDT",
    "RB_USDT",
    "TOOKER_USDT",
    "SPEEDY_USDT",
    "RAIL_USDT",
    "EPIK_USDT",
    "WZRD_USDT",
    "OLM_USDT",
    "ERIC_USDT",
    "INTRO_USDT",
    "CREO_USDT",
    "POON_USDT",
    "AREA_USDT",
    "MICHI_USDT",
    "FLUFF_USDT",
    "BUNNY_USDT",
    "YESBUT_USDT",
    "CATGPT_USDT",
    "MSN_USDT",
    "ELONETH_USDT",
    "LAVA_USDT",
    "DUCKE_USDT",
    "MANEKI_USDT",
    "NOGS_USDT",
    "SKI_USDT",
    "SAFE_USDT",
    "ATR_USDT",
    "MERL_USDT",
    "DEVIN_USDT",
    "FRENS_USDT",
    "GUMMY_USDT",
    "FINDME_USDT",
    "CRODIE_USDT",
    "HAMMY_USDT",
    "USA_USDT",
    "ARKY_USDT",
    "ZEROLEND_USDT",
    "BOOMER_USDT",
    "PINK_USDT",
    "ANYONE_USDT",
    "COOL_USDT",
    "TIM_USDT",
    "MONKE_USDT",
    "PIKA_USDT",
    "SPEED_USDT",
    "BUBBLE_USDT",
    "TRUMPWIF_USDT",
    "AIUS_USDT",
    "ROGER_USDT",
    "MIKI_USDT",
    "DONALDCAT_USDT",
    "SLOTH_USDT",
    "CHUD_USDT",
    "KABAL_USDT",
    "MARU_USDT",
    "TILLY_USDT",
    "IBOSS_USDT",
    "XIAO_USDT",
    "ARGSOL_USDT",
    "SOLCEX_USDT",
    "CTA_USDT",
    "MEX_USDT",
    "RBX_USDT",
    "DWP_USDT",
    "GIL_USDT",
    "GMEETH_USDT",
    "KITTY_USDT",
    "EGLD_USDT",
    "BEBE_USDT",
    "MAGA_USDT",
    "DRIFT_USDT",
    "REEE_USDT",
    "TOBI_USDT",
    "SKATECAT_USDT",
    "POSEIDON_USDT",
    "SELFIE_USDT",
    "BEPE_USDT",
    "PFCC_USDT",
    "HABIBI_USDT",
    "COST_USDT",
    "TESTSOL_USDT",
    "AMCSOL_USDT",
    "FOFAR_USDT",
    "NVDA_USDT",
    "WSBSOL_USDT",
    "BAJU_USDT",
    "NIM_USDT",
    "NOHAT_USDT",
    "COUPE_USDT",
    "FUACK_USDT",
    "NIGHT_USDT",
    "MOOCAT_USDT",
    "WIFMAGA_USDT",
    "SHOE_USDT",
    "BUILD_USDT",
    "NIGI_USDT",
    "ZACK_USDT",
    "GOME_USDT",
    "NAMI_USDT",
    "KIKI_USDT",
    "FFIE_USDT",
    "HODL_USDT",
    "BAZINGA_USDT",
    "MOTHER_USDT",
    "MOJO_USDT",
    "PEW_USDT",
    "CAT_USDT",
    "GROYPER_USDT",
    "ULTRA_USDT",
    "ASTR_USDT",
    "MAGASOL_USDT",
    "ABI_USDT",
    "BEERSOL_USDT",
    "PEPESOLCOMM_USDT",
    "ZION_USDT",
    "HUGH_USDT",
    "PEPEBASE_USDT",
    "XB_USDT",
    "MAMBA_USDT",
    "MCOIN_USDT",
    "HONKETH_USDT",
    "HAPPY_USDT",
    "COK_USDT",
    "TMANIA_USDT",
    "MOTH_USDT",
    "BIRDDOG_USDT",
    "STACKS_USDT",
    "FREESOL_USDT",
    "DAVIDO_USDT",
    "OPPIE_USDT",
    "MAGAPEPE_USDT",
    "WALTER_USDT",
    "CATFROG_USDT",
    "KENDU_USDT",
    "CHAN_USDT",
    "BULEI_USDT",
    "DADDY_USDT",
    "PIZZA_USDT",
    "RCH_USDT",
    "RNT_USDT",
    "DUKO_USDT",
    "SPHYNX_USDT",
    "SPURDOETH_USDT",
    "PEIPEI_USDT",
    "WYAC_USDT",
    "XDC_USDT",
    "MACHO_USDT",
    "TROG_USDT",
    "BOBO_USDT",
    "HAWKTUAH_USDT",
    "SCRAT_USDT",
    "NOTCOIN_USDT",
    "APECOIN_USDT",
    "CHIPPY_USDT",
    "TRUMPNS_USDT",
    "ZRO_USDT",
    "XZK_USDT",
    "KAIKEN_USDT",
    "DJT_USDT",
    "DED_USDT",
    "BILLYSOL_USDT",
    "WOLFSOL_USDT",
    "ZK_USDT",
    "GENIE_USDT",
    "LILPUMP_USDT",
    "OLYMPE_USDT",
    "DOOGLE_USDT",
    "GIOVE_USDT",
    "BARRON_USDT",
    "MOCA_USDT",
    "FLAPPY_USDT",
    "RIS_USDT",
    "DOGGS_USDT",
    "SPIKE_USDT",
    "CAD_USDT",
    "TRUTH_USDT",
    "MEOWCOIN_USDT",
    "SANSHU_USDT",
    "FISH_USDT",
    "WATER_USDT",
    "PEPER_USDT",
    "MIGGLES_USDT",
    "TRUMPAMANIA_USDT",
    "BILL_USDT",
    "SWAG_USDT",
    "FEARNOT_USDT",
    "RETARDIO_USDT",
    "PIXFI_USDT",
    "UXLINK_USDT",
    "A8_USDT",
    "BLAST_USDT",
    "FIGHTSOL_USDT",
    "LWOLF_USDT",
    "NPC_USDT",
    "FIGHT_USDT",
    "EAR_USDT",
    "BWORM_USDT",
    "PARRY_USDT",
    "LRDS_USDT",
    "KAMA_USDT",
    "DELON_USDT",
    "LOLSOL_USDT",
]
if __name__ == "__main__":
    structure_triangular_pairs(coin_list)
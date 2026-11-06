# Automated RFC 8259 & WHATWG EventSource Formal State-Lattice Type Stubs
from typing import Generic, Protocol, TypeVar, Union, Tuple

T_In = TypeVar('T_In')
T_Out = TypeVar('T_Out')

class FrameLatticeNode_00(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x732DE1163E4E
    def transition_00(
        self,
        frame_a: 'FrameLatticeNode_07[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_19[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_37[T_Out, T_In], FrameLatticeNode_07[T_In, T_Out]]': ...

class FrameLatticeNode_01(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x20585C82F972
    def transition_01(
        self,
        frame_a: 'FrameLatticeNode_08[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_20[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_38[T_Out, T_In], FrameLatticeNode_08[T_In, T_Out]]': ...

class FrameLatticeNode_02(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xC6D94390BEBC
    def transition_02(
        self,
        frame_a: 'FrameLatticeNode_09[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_21[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_39[T_Out, T_In], FrameLatticeNode_09[T_In, T_Out]]': ...

class FrameLatticeNode_03(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xFD0F51DB3599
    def transition_03(
        self,
        frame_a: 'FrameLatticeNode_10[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_22[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_40[T_Out, T_In], FrameLatticeNode_10[T_In, T_Out]]': ...

class FrameLatticeNode_04(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x5E7CBC2807BA
    def transition_04(
        self,
        frame_a: 'FrameLatticeNode_11[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_23[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_41[T_Out, T_In], FrameLatticeNode_11[T_In, T_Out]]': ...

class FrameLatticeNode_05(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xD4EFA3151B7D
    def transition_05(
        self,
        frame_a: 'FrameLatticeNode_12[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_24[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_42[T_Out, T_In], FrameLatticeNode_12[T_In, T_Out]]': ...

class FrameLatticeNode_06(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x1D1DD3669E4F
    def transition_06(
        self,
        frame_a: 'FrameLatticeNode_13[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_25[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_43[T_Out, T_In], FrameLatticeNode_13[T_In, T_Out]]': ...

class FrameLatticeNode_07(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x5361E906C95E
    def transition_07(
        self,
        frame_a: 'FrameLatticeNode_14[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_26[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_44[T_Out, T_In], FrameLatticeNode_14[T_In, T_Out]]': ...

class FrameLatticeNode_08(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xCF0269FCFC6A
    def transition_08(
        self,
        frame_a: 'FrameLatticeNode_15[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_27[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_45[T_Out, T_In], FrameLatticeNode_15[T_In, T_Out]]': ...

class FrameLatticeNode_09(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xF1F4E11B24B8
    def transition_09(
        self,
        frame_a: 'FrameLatticeNode_16[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_28[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_46[T_Out, T_In], FrameLatticeNode_16[T_In, T_Out]]': ...

class FrameLatticeNode_10(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xDD9021D6D1C1
    def transition_10(
        self,
        frame_a: 'FrameLatticeNode_17[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_29[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_47[T_Out, T_In], FrameLatticeNode_17[T_In, T_Out]]': ...

class FrameLatticeNode_11(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x22CFC74E710B
    def transition_11(
        self,
        frame_a: 'FrameLatticeNode_18[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_30[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_48[T_Out, T_In], FrameLatticeNode_18[T_In, T_Out]]': ...

class FrameLatticeNode_12(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xC79A229FA8A0
    def transition_12(
        self,
        frame_a: 'FrameLatticeNode_19[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_31[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_49[T_Out, T_In], FrameLatticeNode_19[T_In, T_Out]]': ...

class FrameLatticeNode_13(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xF0A305ACD814
    def transition_13(
        self,
        frame_a: 'FrameLatticeNode_20[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_32[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_50[T_Out, T_In], FrameLatticeNode_20[T_In, T_Out]]': ...

class FrameLatticeNode_14(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xC7CE425B0F11
    def transition_14(
        self,
        frame_a: 'FrameLatticeNode_21[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_33[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_51[T_Out, T_In], FrameLatticeNode_21[T_In, T_Out]]': ...

class FrameLatticeNode_15(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xCD023B05A933
    def transition_15(
        self,
        frame_a: 'FrameLatticeNode_22[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_34[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_52[T_Out, T_In], FrameLatticeNode_22[T_In, T_Out]]': ...

class FrameLatticeNode_16(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x483AD60BDFFA
    def transition_16(
        self,
        frame_a: 'FrameLatticeNode_23[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_35[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_53[T_Out, T_In], FrameLatticeNode_23[T_In, T_Out]]': ...

class FrameLatticeNode_17(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xF0AF8F3035EE
    def transition_17(
        self,
        frame_a: 'FrameLatticeNode_24[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_36[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_54[T_Out, T_In], FrameLatticeNode_24[T_In, T_Out]]': ...

class FrameLatticeNode_18(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x9447DA80EA61
    def transition_18(
        self,
        frame_a: 'FrameLatticeNode_25[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_37[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_55[T_Out, T_In], FrameLatticeNode_25[T_In, T_Out]]': ...

class FrameLatticeNode_19(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xD2B2CF23A6AD
    def transition_19(
        self,
        frame_a: 'FrameLatticeNode_26[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_38[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_56[T_Out, T_In], FrameLatticeNode_26[T_In, T_Out]]': ...

class FrameLatticeNode_20(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xC4086195B0E1
    def transition_20(
        self,
        frame_a: 'FrameLatticeNode_27[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_39[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_57[T_Out, T_In], FrameLatticeNode_27[T_In, T_Out]]': ...

class FrameLatticeNode_21(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xAEDEA22E2D9E
    def transition_21(
        self,
        frame_a: 'FrameLatticeNode_28[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_40[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_58[T_Out, T_In], FrameLatticeNode_28[T_In, T_Out]]': ...

class FrameLatticeNode_22(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x7C8BA7E6D329
    def transition_22(
        self,
        frame_a: 'FrameLatticeNode_29[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_41[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_59[T_Out, T_In], FrameLatticeNode_29[T_In, T_Out]]': ...

class FrameLatticeNode_23(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x0002D5E44A84
    def transition_23(
        self,
        frame_a: 'FrameLatticeNode_30[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_42[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_60[T_Out, T_In], FrameLatticeNode_30[T_In, T_Out]]': ...

class FrameLatticeNode_24(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x7BA61DB0F3D5
    def transition_24(
        self,
        frame_a: 'FrameLatticeNode_31[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_43[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_61[T_Out, T_In], FrameLatticeNode_31[T_In, T_Out]]': ...

class FrameLatticeNode_25(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x619D791E7D06
    def transition_25(
        self,
        frame_a: 'FrameLatticeNode_32[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_44[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_62[T_Out, T_In], FrameLatticeNode_32[T_In, T_Out]]': ...

class FrameLatticeNode_26(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x29A4362611AC
    def transition_26(
        self,
        frame_a: 'FrameLatticeNode_33[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_45[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_63[T_Out, T_In], FrameLatticeNode_33[T_In, T_Out]]': ...

class FrameLatticeNode_27(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xF7C05E07CBD2
    def transition_27(
        self,
        frame_a: 'FrameLatticeNode_34[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_46[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_00[T_Out, T_In], FrameLatticeNode_34[T_In, T_Out]]': ...

class FrameLatticeNode_28(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x22169ABB1655
    def transition_28(
        self,
        frame_a: 'FrameLatticeNode_35[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_47[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_01[T_Out, T_In], FrameLatticeNode_35[T_In, T_Out]]': ...

class FrameLatticeNode_29(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x6AACE40610CE
    def transition_29(
        self,
        frame_a: 'FrameLatticeNode_36[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_48[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_02[T_Out, T_In], FrameLatticeNode_36[T_In, T_Out]]': ...

class FrameLatticeNode_30(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x397DDB59E388
    def transition_30(
        self,
        frame_a: 'FrameLatticeNode_37[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_49[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_03[T_Out, T_In], FrameLatticeNode_37[T_In, T_Out]]': ...

class FrameLatticeNode_31(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xA93344C5D631
    def transition_31(
        self,
        frame_a: 'FrameLatticeNode_38[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_50[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_04[T_Out, T_In], FrameLatticeNode_38[T_In, T_Out]]': ...

class FrameLatticeNode_32(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x0AF5651E7C67
    def transition_32(
        self,
        frame_a: 'FrameLatticeNode_39[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_51[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_05[T_Out, T_In], FrameLatticeNode_39[T_In, T_Out]]': ...

class FrameLatticeNode_33(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x54250B02DD49
    def transition_33(
        self,
        frame_a: 'FrameLatticeNode_40[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_52[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_06[T_Out, T_In], FrameLatticeNode_40[T_In, T_Out]]': ...

class FrameLatticeNode_34(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x312D3E906338
    def transition_34(
        self,
        frame_a: 'FrameLatticeNode_41[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_53[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_07[T_Out, T_In], FrameLatticeNode_41[T_In, T_Out]]': ...

class FrameLatticeNode_35(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xEC33F95E8DCE
    def transition_35(
        self,
        frame_a: 'FrameLatticeNode_42[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_54[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_08[T_Out, T_In], FrameLatticeNode_42[T_In, T_Out]]': ...

class FrameLatticeNode_36(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xF31332E117AA
    def transition_36(
        self,
        frame_a: 'FrameLatticeNode_43[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_55[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_09[T_Out, T_In], FrameLatticeNode_43[T_In, T_Out]]': ...

class FrameLatticeNode_37(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xE51E1F1F51F3
    def transition_37(
        self,
        frame_a: 'FrameLatticeNode_44[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_56[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_10[T_Out, T_In], FrameLatticeNode_44[T_In, T_Out]]': ...

class FrameLatticeNode_38(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xB375DFE456AF
    def transition_38(
        self,
        frame_a: 'FrameLatticeNode_45[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_57[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_11[T_Out, T_In], FrameLatticeNode_45[T_In, T_Out]]': ...

class FrameLatticeNode_39(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xBD3EE0059887
    def transition_39(
        self,
        frame_a: 'FrameLatticeNode_46[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_58[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_12[T_Out, T_In], FrameLatticeNode_46[T_In, T_Out]]': ...

class FrameLatticeNode_40(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xF5312B6D7C83
    def transition_40(
        self,
        frame_a: 'FrameLatticeNode_47[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_59[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_13[T_Out, T_In], FrameLatticeNode_47[T_In, T_Out]]': ...

class FrameLatticeNode_41(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x7A42B0C1FEBB
    def transition_41(
        self,
        frame_a: 'FrameLatticeNode_48[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_60[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_14[T_Out, T_In], FrameLatticeNode_48[T_In, T_Out]]': ...

class FrameLatticeNode_42(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xCC1AD5BCF09E
    def transition_42(
        self,
        frame_a: 'FrameLatticeNode_49[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_61[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_15[T_Out, T_In], FrameLatticeNode_49[T_In, T_Out]]': ...

class FrameLatticeNode_43(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x6983D75309A1
    def transition_43(
        self,
        frame_a: 'FrameLatticeNode_50[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_62[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_16[T_Out, T_In], FrameLatticeNode_50[T_In, T_Out]]': ...

class FrameLatticeNode_44(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x784A60479E82
    def transition_44(
        self,
        frame_a: 'FrameLatticeNode_51[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_63[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_17[T_Out, T_In], FrameLatticeNode_51[T_In, T_Out]]': ...

class FrameLatticeNode_45(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x93D8845FD3E6
    def transition_45(
        self,
        frame_a: 'FrameLatticeNode_52[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_00[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_18[T_Out, T_In], FrameLatticeNode_52[T_In, T_Out]]': ...

class FrameLatticeNode_46(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x8638D429036F
    def transition_46(
        self,
        frame_a: 'FrameLatticeNode_53[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_01[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_19[T_Out, T_In], FrameLatticeNode_53[T_In, T_Out]]': ...

class FrameLatticeNode_47(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xA7E7F237EAAE
    def transition_47(
        self,
        frame_a: 'FrameLatticeNode_54[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_02[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_20[T_Out, T_In], FrameLatticeNode_54[T_In, T_Out]]': ...

class FrameLatticeNode_48(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xD0C1BE4054D3
    def transition_48(
        self,
        frame_a: 'FrameLatticeNode_55[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_03[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_21[T_Out, T_In], FrameLatticeNode_55[T_In, T_Out]]': ...

class FrameLatticeNode_49(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xEB5C151AB232
    def transition_49(
        self,
        frame_a: 'FrameLatticeNode_56[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_04[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_22[T_Out, T_In], FrameLatticeNode_56[T_In, T_Out]]': ...

class FrameLatticeNode_50(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x5B70C38FACF5
    def transition_50(
        self,
        frame_a: 'FrameLatticeNode_57[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_05[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_23[T_Out, T_In], FrameLatticeNode_57[T_In, T_Out]]': ...

class FrameLatticeNode_51(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x4FCF308061CF
    def transition_51(
        self,
        frame_a: 'FrameLatticeNode_58[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_06[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_24[T_Out, T_In], FrameLatticeNode_58[T_In, T_Out]]': ...

class FrameLatticeNode_52(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x61B3DBFB56C9
    def transition_52(
        self,
        frame_a: 'FrameLatticeNode_59[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_07[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_25[T_Out, T_In], FrameLatticeNode_59[T_In, T_Out]]': ...

class FrameLatticeNode_53(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x8F882B5663D5
    def transition_53(
        self,
        frame_a: 'FrameLatticeNode_60[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_08[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_26[T_Out, T_In], FrameLatticeNode_60[T_In, T_Out]]': ...

class FrameLatticeNode_54(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xF2C76D3A1780
    def transition_54(
        self,
        frame_a: 'FrameLatticeNode_61[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_09[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_27[T_Out, T_In], FrameLatticeNode_61[T_In, T_Out]]': ...

class FrameLatticeNode_55(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xD9E32BB0AACF
    def transition_55(
        self,
        frame_a: 'FrameLatticeNode_62[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_10[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_28[T_Out, T_In], FrameLatticeNode_62[T_In, T_Out]]': ...

class FrameLatticeNode_56(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x6FC3EDBBA54F
    def transition_56(
        self,
        frame_a: 'FrameLatticeNode_63[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_11[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_29[T_Out, T_In], FrameLatticeNode_63[T_In, T_Out]]': ...

class FrameLatticeNode_57(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x0689D6A7C76A
    def transition_57(
        self,
        frame_a: 'FrameLatticeNode_00[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_12[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_30[T_Out, T_In], FrameLatticeNode_00[T_In, T_Out]]': ...

class FrameLatticeNode_58(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x31D52D8C8658
    def transition_58(
        self,
        frame_a: 'FrameLatticeNode_01[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_13[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_31[T_Out, T_In], FrameLatticeNode_01[T_In, T_Out]]': ...

class FrameLatticeNode_59(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x012D3595B1D5
    def transition_59(
        self,
        frame_a: 'FrameLatticeNode_02[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_14[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_32[T_Out, T_In], FrameLatticeNode_02[T_In, T_Out]]': ...

class FrameLatticeNode_60(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x36DF9D114650
    def transition_60(
        self,
        frame_a: 'FrameLatticeNode_03[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_15[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_33[T_Out, T_In], FrameLatticeNode_03[T_In, T_Out]]': ...

class FrameLatticeNode_61(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x8BADF1256929
    def transition_61(
        self,
        frame_a: 'FrameLatticeNode_04[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_16[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_34[T_Out, T_In], FrameLatticeNode_04[T_In, T_Out]]': ...

class FrameLatticeNode_62(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x404DC5739E19
    def transition_62(
        self,
        frame_a: 'FrameLatticeNode_05[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_17[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_35[T_Out, T_In], FrameLatticeNode_05[T_In, T_Out]]': ...

class FrameLatticeNode_63(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x95CE615C811A
    def transition_63(
        self,
        frame_a: 'FrameLatticeNode_06[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_18[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_36[T_Out, T_In], FrameLatticeNode_06[T_In, T_Out]]': ...

